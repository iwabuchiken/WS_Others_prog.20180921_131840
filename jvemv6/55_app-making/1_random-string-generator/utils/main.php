<?php

	date_default_timezone_set('Asia/Tokyo');

	$time_label = date("H:i:s");
	//$date_label = date("d/m/Y H:i:s");
	$date_label = date("Y/m/d H:i:s");
	
	$date_label_serial = date("Ymd_His");

	echo '<div class="time_label">
				<!-- <input -->
				<input
					id="time_label"
					name="time_label"
					
					onmouseover="this.select();"
					size="7"
					type="text"
					value="'.$time_label.'" 
					
					class="input_area"/>
							
				<input
					id="date_label"
					name="date_label"
					
					onmouseover="this.select();"
					size="20"
					type="text"
					value="'.$date_label.'" 
					
					class="input_area"/>
					
				<input
					id="date_label_serial"
					name="date_label_serial"
					
					onmouseover="this.select();"
					size="20"
					type="text"
					value="'.$date_label_serial.'" 
					
					class="input_area"/>

							
			</div>';

?>