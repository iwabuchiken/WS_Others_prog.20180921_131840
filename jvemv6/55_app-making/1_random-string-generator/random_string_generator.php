<html>

	<head>
		<title>
		
			random_string_generator.php	
		
		</title>

		<meta name="viewport"
	           content="width=device-width,
				user-scalable=yes,
				initial-scale=0.8,
	                    maximum-scale=3.0" />

		<script src="http://code.jquery.com/jquery-2.0.3.min.js"></script>
		
		<link rel="stylesheet" href="./stylesheet/url_encode_decode.css" type="text/css">
		
		<script type="text/javascript" src="./javascript/main.js"></script>
	
	</head>
	
	<body>
	
<!-- 		<textarea rows="10" cols="10" id="ta_encode"> -->
		<div>
		
			<textarea rows="1" id="ta_disp_string" onmouseover="this.select()"></textarea>
			
		</div>
		
		<br>
		<br>
		
		<div>
		
			<button onclick="generate_random_string();">Generate</button>
		
		</div>
		
		<br>

		<div>
		
			<textarea rows="1" id="ta_numof_chars" onmouseover="this.select()">4</textarea>
			
		</div>
		
		<br>
		<br>
		<div>
		
			<a href="http://benfranklin.chips.jp/PHP_server/D-2/time_calc.php"
				target="_blank"
				>
				time_calc.php
			</a>
		
		</div>
		
	</body>

</html>