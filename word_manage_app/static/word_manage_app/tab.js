$(".tab_label").on("click",function(){
	alert("tab custmization js is called here");

	var $th = $(this).index();
	$(".tab_label").removeClass("active");
	$(".tab_panel").removeClass("active");
	$(this).addClass("active");
	$(".tab_panel").eq($th).addClass("active");
});
