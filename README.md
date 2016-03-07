Deaf Grandpa with AJAX
======================

Ready for some [Asynchronous Javascript and XML](http://en.wikipedia.org/wiki/Ajax_programming)?

We're going to be talking to Grandpa again, but this time the request is going to be made asynchronously. We can send it to the server without reloading the page.

#### Files

Take a look at our main template - we've got JQuery, the `grandpa.js` file we're going to write our javascript in, and a file called `django_ajax.js` that handles the csrf_token. You can figure out what it does but don't touch it.

#### Instructions

We're going to be using jQuery, specifically [$.post()](http://api.jquery.com/jquery.post/)

This is basically what it's going to look like:
```js
	$('#grandpa_form').submit(function(event){ //form submit event handler
		event.preventDefault(); //prevents default which would reload page
		//post form to server, get data back
		$.post( "/", $( "#grandpa_form" ).serialize(), function(data){
			//do something
		});
	})
```
We're also going to need to write our get and post routes similarly to how we wrote them the last time we did Deaf Grandpa, with the main difference being that instead of redirecting on POST, we're going to return JSON.

#### Tips

As a general rule for Ajax in 2015 we want to return JSON from the server to be used on the front-end.

Using Django's JsonResponse, have your server return a JSON object to jQuery. Parse the object in jQuery and display Grandpa's response to the user.
