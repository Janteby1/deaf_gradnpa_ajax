
$(document).ready(function(){
  console.log("Hi there!")

  $('#submit_grandpa').on('click', function(event){ //form submit event handler
    event.preventDefault();//prevents default which would reload page

    // this is the value from the form 
    var input = $('input[name="said"]').val()
    console.log(input);

    // var data = $("#say_grandpa").serialize() // returns all the data in your form
    // console.log(data);

    var data = {
        "data":input
    };
    data = JSON.stringify(data);

    // sending the data to the url then view
    $.ajax({
        method: "POST",
        url: "http://localhost:8000/home",
        data: data,
        // dataType: "jsonp", # only needed if we are going ot a different URL
        // alternative syntax
        // $.post( "/", $( "#grandpa_form" ).serialize(), function(data){


      // comes back from the view with a json respone to our data 
      success:function(response){
        console.log(response)
        // basicallly prints it out by attaching it to a div
        $('.grandpa').text(response["msg"])
        // $('.grandpa').empty();
        // $('.grandpa').append(response["msg"])
      }
    })
  })
})



