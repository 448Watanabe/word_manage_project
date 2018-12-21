function myFunction2() {
	alert("this is onclick Test2");
}

console.log("myFunction2 is called here:");


function myFunction3(){
	console.log("myFunction3 is called:");
	var $th = $(this).index();
	console.log($th);

	$(".clickTest").click(function(){
		console.log("onclick function is called:");
	});
}