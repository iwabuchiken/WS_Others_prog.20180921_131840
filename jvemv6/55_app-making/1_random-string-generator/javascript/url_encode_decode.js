$(document).ready(function(){

//	alert("ready");
	
//	$('#ta_encode').change(function(){
//		
//		alert("changed");
//		
//	});
	
})

//ref https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_oninput
function encode_text() {

	var input = $('#ta_encode').val();
//	var input = $('#ta_encode').value;
	
//	alert("your input => " + input);
	
	//ref https://www.sitepoint.com/jquery-decode-url-string/
	var input_encoded = encodeURIComponent(input);
	
	// set the text
	//ref http://stackoverflow.com/questions/415602/set-value-of-textarea-in-jquery answered Jan 6 '09 at 6:10
	$('#ta_decode').val(input_encoded);
//	$('#ta_decode').val(input);
	
}//encode_text()

function decode_text() {
	
	var input = $('#ta_decode').val();
//	var input = $('#ta_encode').value;
	
//	alert("your input => " + input);
	
	var input_decoded = decodeURIComponent(input);
	
	// set the text
	$('#ta_encode').val(input_decoded);
//	$('#ta_decode').val(input);
	
}//decode_text()

function clear_all() {
	
//	alert("clearing...");
	
	$('#ta_encode').val("");
	$('#ta_decode').val("");
	
}//clear_all()

function copy_encoded() {
	
    $("#ta_encode").select();
    
    document.execCommand('copy');
    
    $("#bt_copy_encoded").fadeOut(70).fadeIn(100);
    
//    alert("copied");
	
}//copy_encoded()

function copy_decoded() {
	
	$("#ta_decode").select();
	
	//ref http://stackoverflow.com/questions/37658524/copying-text-of-textarea-in-clipboard-when-button-is-clicked answered Jun 6 '16 at 13:55
	document.execCommand('copy');
	
	var elem = $("#ta_decode");
//	var elem = $("#bt_copy_decoded");
	
	var oldBG = elem.css('backgroundColor');
	
//	alert("old BG => " + oldBG);
	
	//ref http://stackoverflow.com/questions/3003819/possible-to-change-background-color-onclick-then-automatically-change-back-a-se asked Jun 9 '10 at 7:27
//    elem.css('backgroundColor', '#FFFFFF').delay(1000).css('backgroundColor', oldBG);	//=> n.w.
//    elem.css('background', '#FFFFFF').delay(1000).css('background', oldBG);	//=> n.w.
//    elem.css('background-color', '#FFFFFF').delay(1000).css('background-color', oldBG);	//=> n.w.
//    elem.css('background-color', 'red');	//=> w.
//    elem.css('background-color', 'red').delay(1000).css('background-color', 'yellow');	//=> n.w. 
//    elem.css('background-color', 'red').delay(3000).css('background-color', 'yellow');	//=> n.w.
    
	//ref http://stackoverflow.com/questions/4544126/jquery-delay-not-working answered Dec 28 '10 at 6:35 
//	elem.css('background-color', 'red');
//	elem.css('background-color', 'gray');
	elem.css('background-color', '#DDDCA9');
	var time_out = 50;
//	var time_out = 100;
	setTimeout(function() {					//=> working!
//	    trans.addClass('not_transparent');
//		elem.css('background-color', 'yellow')
		elem.css('background-color', oldBG)
		
	}, time_out);
//}, 1000);
	
	//ref http://stackoverflow.com/questions/275931/how-do-you-make-an-element-flash-in-jquery answered Feb 1 '12 at 14:19
	$("#bt_copy_decoded").fadeOut(70).fadeIn(100);
	
//	$("#bt_copy_decoded").fadeOut(100).fadeIn(100).fadeOut(100).fadeIn(100);
//	$("#bt_copy_decoded").fadeIn(100).fadeOut(100).fadeIn(100);
//	$("#bt_copy_decoded").fadeIn(100).fadeOut(100).fadeIn(100).fadeOut(100).fadeIn(100);
//	$("#ta_decode").fadeIn(100).fadeOut(100).fadeIn(100).fadeOut(100).fadeIn(100);
	
//	alert("copied");
	
}//copy_decoded()


