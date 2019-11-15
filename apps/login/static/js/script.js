$(document).ready(function () {
    console.log("In doc ready");
    $('#email').keyup(function () {
        console.log("In keyup");
        var data = $("#regForm").serialize(); // capture all the data in the form in the variable data
        $.ajax({
                method: "POST", // we are using a post request here, but this could also be done with a get
                url: "/email",
                data: data
            })
            .done(function (res) {
                console.log("function");
                // console.log(res); 
                $("#emailMsg").html(res); // manipulate the dom when the response comes back
            });
    });
});