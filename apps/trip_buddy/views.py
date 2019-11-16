from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.


def dashboard(request):
    cur_user = User.objects.get(id=request.session["userid"])
    other_user = User.objects.exclude(id=request.session["userid"])
    trips_not_created = Trip.objects.exclude(user=cur_user.id)
    trips_not_joined = Trip.objects.exclude(joined_by=cur_user.id)
    trips_not_joined_not_created = trips_not_joined.exclude(user=cur_user.id)
    context = {
        "all_trips": Trip.objects.all(),
        "user_trips": cur_user.create_trips.values(),
        "trips_not_joined_not_created": trips_not_joined_not_created,
        "trip_joined": cur_user.join.values(),
    }
    # print(context["all_trips"].values())
    return render(request, "trip_buddy/dashboard.html", context)


def edit(request, number):
    context = {
        "number": number,
        "trip": Trip.objects.get(id=number)
    }
    context["trip"].start_date = context["trip"].start_date.strftime(
        '%Y-%m-%d')
    context["trip"].end_date = context["trip"].end_date.strftime(
        '%Y-%m-%d')
    if request.method == "POST":
        errors = Trip.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            print(errors)
            return redirect(f'/trips/edit/{number}')
        else:
            trip = Trip.objects.get(id=number)
            trip.destination = request.POST["destination"]
            trip.start_date = request.POST["start_date"]
            trip.end_date = request.POST["end_date"]
            trip.plan = request.POST["plan"]
            trip.save()
            return redirect("/dashboard")
    else:
        return render(request, "trip_buddy/update.html", context)


def add(request):
    # if the errors object is empty, that means there were no errors!
    if request.method == "POST":
        # pass the post data to the method we wrote and save the response in a variable called errors
        errors = Trip.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it

        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                # Adding errors into messages
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            print(errors)
            return redirect('/trips/new')
        else:
            cur_user = User.objects.get(id=request.session["userid"])
            Trip.objects.create(destination=request.POST["destination"], start_date=request.POST["start_date"],
                                end_date=request.POST["end_date"], plan=request.POST["plan"], user=cur_user)
            messages.success(request, "Trip successfully created")
            return redirect("/dashboard")
    else:
        return render(request, "trip_buddy/create.html")


def show(request, number):
    trip = Trip.objects.get(id=number)

    context = {
        'trip': Trip.objects.get(id=number),
        'joined_by': trip.joined_by.values(),
    }

    return render(request, "trip_buddy/read.html", context)


def delete(request, number):
    trip = Trip.objects.get(id=number)
    trip.delete()
    return redirect("/dashboard")


# Black belt features
def join(request, trip_id):
    cur_user = User.objects.get(id=request.session["userid"])
    trip = Trip.objects.get(id=trip_id)
    cur_user.join.add(trip)
    print(cur_user.join.values())

    return redirect("/dashboard")


def cancel(request, trip_id):
    cur_user = User.objects.get(id=request.session["userid"])
    trip = Trip.objects.get(id=trip_id)
    trip.joined_by.remove(cur_user)
    return redirect("/dashboard")
