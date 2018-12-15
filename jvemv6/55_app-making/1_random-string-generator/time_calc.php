<!-- 

git merge => http://qiita.com/takanatsu/items/fc89de9bd11148da1438


 -->

<?php require "partials/partial_1.php"?>
<html>
<head>
	
	<title><?php echo basename(__FILE__); ?></title>
	
	<meta name="viewport"
           content="width=device-width,
			user-scalable=yes,
			initial-scale=0.8,
                    maximum-scale=3.0" />

	<link rel="stylesheet" href="./stylesheet/main.css" type="text/css">
                    
	<script src="http://code.jquery.com/jquery-2.0.3.min.js"></script>

	<!-- http://www.pori2.net/js/kihon/16.html -->
	<script type="text/javascript" src="./javascript/main.js"></script>
	
</head>

<?php

	//REF http://www.4web8.com/2581.html
	date_default_timezone_set('Asia/Tokyo');
	
// 	setlocale(LC_ALL, 'nl_NL');

	$current = time();
	
	$date_label = date("d/m/Y H:i:s");
	$date_only_label = date("d/m/Y");
	$time_label = date("H:i:s");
	$time_label_serial = date("Ymd_His");

	
?>

<!-- REF focus() http://www.mediacollege.com/internet/javascript/form/focus.html -->
<body onLoad="document.time_form.time_label.focus();">
<!-- <body onLoad="document.time_form.time_label.focus(); show_msg();"> -->
<!-- <body onLoad="document.time_form.date_label.focus();"> -->

	<?php show_time_data_table();?>

	<hr/>
	
	<div id="js_area">
		<!-- Javascript area -->
	
		<!-- http://homepage3.nifty.com/aya_js/js2/js214.htm -->
		<!--  <INPUT TYPE="button" VALUE="GO" ONCLICK="set_msg();"> -->
		
		
		<INPUT TYPE="image"
				src="images/halte-session-icone-4911-32.png"
				ONCLICK="clear_msg();"
				
				>
		
		&nbsp; &nbsp;
		
		<INPUT TYPE="image"
				src="images/chronometre-icone-4052-32.png"
				ONCLICK="set_msg();"
				ONCLICK="set_msg();"
				>
				
		&nbsp; &nbsp;

		<INPUT TYPE="image"
				src="images/refresh.png"
				ONCLICK="page_reload();">
		
<!-- 		<a href="http://benfranklin.chips.jp/PHP_server/D-2/url_encode_decode.php">a --- %</a> -->
		
		<div><b>Times</b></div>
		<div id="js"></div>
		
		<div style="text-align: right; margin-right: 50px;">
			
			<a href="http://benfranklin.chips.jp/PHP_server/D-2/url_encode_decode.php"
				target="_blank"
				>
				encode/decode
			</a>

			<br>
			<a href="http://benfranklin.chips.jp/PHP_server/D-2/random_string_generator.php"
				target="_blank"
				>
				random_string_generator.php
			</a>
		
		</div>
		
	</div>
</body>

</html>