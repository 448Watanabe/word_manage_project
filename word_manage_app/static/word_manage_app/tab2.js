$(".tab_panel").on("click",function(){
	console.log("onclick function is called:");

	var $th = $(this).index();
	$(".tab_label").removeClass("active");
	$(".tab_panel").removeClass("active");
	$(this).addClass("active");
	$(".tab_panel").eq($th).addClass("active");
});

console.log("tab2.js is loaded:");
