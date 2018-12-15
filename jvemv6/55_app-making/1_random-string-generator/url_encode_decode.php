<html>

	<head>
		<title>
		
			url_encode-decode	
		
		</title>

		<meta name="viewport"
	           content="width=device-width,
				user-scalable=yes,
				initial-scale=0.8,
	                    maximum-scale=3.0" />

		<script src="http://code.jquery.com/jquery-2.0.3.min.js"></script>
		
		<link rel="stylesheet" href="./stylesheet/url_encode_decode.css" type="text/css">
		
		<script type="text/javascript" src="./javascript/url_encode_decode.js"></script>
	
	</head>
	
	<body>
	
<!-- 		<textarea rows="10" cols="10" id="ta_encode"> -->
		<div>
		
			<textarea rows="10" id="ta_encode" oninput="encode_text()" onmouseover="this.select()"></textarea>
			
<!-- 			<textarea rows="10" cols="10" id="ta_decode"> -->
			<textarea id="ta_decode" oninput="decode_text()" onmouseover="this.select()"></textarea>
		</div>
		
		<div>
			<input type="button" value="Copy" id="bt_copy_encoded" onclick="copy_encoded()">
			
			<label id="label_encode">Encode</label>
			
<!-- 			<button id="bt_clear_all">clear all</button> -->
			<input type="button" value="clear all" id="bt_clear_all" onclick="clear_all()">
			
			<label id="label_decode">Decode</label>
			
			<input type="button" value="Copy" id="bt_copy_decoded" onclick="copy_decoded()">
		
		
		</div>
	
		<br>
		<br>
		<br>
		<div>
		
			<a href="http://benfranklin.chips.jp/PHP_server/D-2/time_calc.php"
				target="_blank"
				>
				time_calc.php
			</a>
			
			<br>
			<a href="http://benfranklin.chips.jp/PHP_server/D-2/random_string_generator.php"
				target="_blank"
				>
				random_string_generator.php
			</a>
		
		</div>
		
	</body>

</html>