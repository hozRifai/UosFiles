$(document).ready(function(){
	// testing $("h2").hide();
	$("html").niceScroll();
	//here
});

$.ajax({
	url: "http://127.0.0.1:8000/media/documents/",
	success: function(data){
		$(data).find("a:contains(.jpg)").each(function(){
		// will loop through 
		var images = $(this).attr("href");
	$('<p></p>').html(images).appendTo('container')
});
}
});