$(document).ready(function(){
	// testing $("h2").hide();
	$("html").niceScroll();

});

$.ajax({
  url: "http://127.0.0.1:8000/files/dashboard/",
	success: function(data){
    alert("i am here");
    $(data).find("a:contains(.jpg)").each(function(){
    // will loop through 
    var images = $(this).attr("href");
    $('<p></p>').html(images).appendTo('container')
    });
  }
});