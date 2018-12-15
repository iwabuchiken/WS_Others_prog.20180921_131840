function show_msg() {
	
	alert("HI");
	
}

function set_msg() {
	
//	http://www.tohoho-web.com/js/jquery/ajax.htm
	$.ajax({
		
	    url: "./utils/main.php",
	    type: "GET",
	    timeout: 10000
	    
	}).done(function(data, status, xhr) {
		
//	    $("#js").html(data);
//	    $("#js").append(data);
	    $("#js").prepend(data);
//	    $("#js").append("<br/>");
	    
	    
	}).fail(function(xhr, status, error) {
		
	    $("#js").append("xhr.status = " + xhr.status + "<br>");          // 例: 404
	    
	});
	
}//function set_msg() {

function clear_msg() {
	
	targets = $(".time_label");
	
//	http://semooh.jp/jquery/api/manipulation/remove/%5Bexpr%5D/
	targets.remove();
	
}//function clear_msg() {

function page_reload() {
	
	//REF http://www5e.biglobe.ne.jp/access_r/hp/javascript/js_091.html
	window.location.reload();
	
}

function generate_random_string() {
	
//	alert("generating...");
	
	/***************************
		param : num of chars
	 ***************************/
	var tagOf_NumOfChars = $('#ta_numof_chars').val();
	
	//ref http://www.jquerybyexample.net/2013/02/jquery-convert-string-to-integer.html
	var numOf_Chars = parseInt(tagOf_NumOfChars);
//	var numOf_Chars = 4;
	
	console.log("numOf_Chars => " + numOf_Chars + " / " + "numOf_Chars * 2 => " + numOf_Chars * 2);
	
	/***************************
		tag
	 ***************************/
	var tag = $('#ta_disp_string');
	
	/***************************
		gen : random string
	 ***************************/
	var str_Base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
	
	//ref https://www.w3schools.com/jsref/jsref_split.asp "Separate each character"
	var tokenOf_Chars = str_Base.split("");
	
	var lenOf_Token = tokenOf_Chars.length;
	
	console.log("lenOf_Token => " + lenOf_Token);
	
	//ref https://www.w3schools.com/jsref/jsref_random.asp
	var num_Ineger = Math.floor((Math.random() * 36) + 1);
	
	console.log("num_Ineger => " + num_Ineger);
	
	// build string
	var strOf_RandomChars = "";
	
	for (var int = 0; int < numOf_Chars; int++) {
		
		num_Ineger = Math.floor((Math.random() * (lenOf_Token - 1)) + 1);
		
		strOf_RandomChars += tokenOf_Chars[num_Ineger];
		
//		console.log("strOf_RandomChars => " + strOf_RandomChars);
		
	}//for (var int = 0; int < lenOf_Token; int++) {
	
	
	
	/***************************
		set : string
	 ***************************/
	tag.html(strOf_RandomChars);
//	tag.html("yes");
	
	//debug
//	console.log("tag ==> html added");
	
	
}//function generate_random_string() {


// REF Fit the field size to the content http://stackoverflow.com/questions/6819548/onload-fit-input-size-to-length-of-text T.J. Crowder
