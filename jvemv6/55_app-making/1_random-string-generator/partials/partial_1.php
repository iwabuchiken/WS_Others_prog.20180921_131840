<?php 

	function page_reload() {
		
		echo "<i>".__FILE__."</i>";
		
	}
	
	function show_time_data_table() {
		
		//REF http://www.4web8.com/2581.html
		date_default_timezone_set('Asia/Tokyo');
		
		// 	setlocale(LC_ALL, 'nl_NL');
		
		$current = time();
		
		$date_label = date("d/m/Y H:i:s");
		$date_only_label = date("d/m/Y");
		$time_label = date("H:i:s");
		$time_label_serial = date("Ymd_His");
		
		
		echo "		<!--  <table class=\"text-center\"> -->
		<table id=\"time_table\">
			<tr>
				<!-- REF 'this.select()' http://stackoverflow.com/questions/4543236/onclick-select-all-text-in-text-field-rails answered Dec 28 '10 at 2:27 -->
		<!-- 		REF readonly http://www.w3schools.com/tags/tag_input.asp -->
				<td class=\"labels\">
				
					<img alt=\"Date\" src=\"images/calendrier-date-icone-6871-48.png\">

					&nbsp;
					<img alt=\"Time\" src=\"images/chronometre-icone-4052-32.png\">
					
				</td>
				
				<td>
					<input
							id=\"timecal_full\"
							name=\"date_label\"
							onmouseover=\"this.select()\"
							
							type=\"text\"
							value=".$date_label."
							
							
							class=\"input_area\"
							/>
				</td>
			</tr>
			
			<tr>
				<td class=\"labels\">
					<img alt=\"Time\" src=\"images/chronometre-icone-4052-32.png\">
				</td>
				<td>
					<input
							id=\"timecal_full\"
							name=\"time_label\"
							onmouseover=\"this.select()\"
							type=\"text\"
							value=".$time_label." 
							
							class=\"input_area\"/>
				</td>
			</tr>
			
			<tr>
				<td class=\"labels\">
					<img alt=\"Date\" src=\"images/calendrier-date-icone-6871-48.png\">
				</td>
				<td>
					<input
							id=\"timecal_full\"
							name=\"date_only_label\"
							onmouseover=\"this.select()\"
							type=\"text\"
							value=".$date_only_label."
							
							
							class=\"input_area\"
							/>
				</td>
			</tr>
			<tr>
				<td class=\"labels\">
					<img alt=\"Serial\" src=\"images/note-ecrivez-icone-9391-48.png\">
				</td>
				<td>
					<input
							id=\"timecal_full_serial\"
							name=\"time_label_serial\"
							onmouseover=\"this.select()\"
							type=\"text\"
							value=".$time_label_serial." 
							
							class=\"input_area\"/>
				</td>
			</tr>
		</table>";
	
	
	}
?>