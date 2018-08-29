$(document).ready(function(){
	// testing $("h2").hide();
	$("html").niceScroll();
	//here
});

$.ajax({
	url: "https://uosfiles.herokuapp.com/media/documents/",
	success: function(data){
		$(data).find("a:contains(.jpg)").each(function(){
		// will loop through 
		var images = $(this).attr("href");
	$('<p></p>').html(images).appendTo('container')
});
}
});