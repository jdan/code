<?php

class CompetitionReport extends Alert {
	
	protected function generateAlert() {
		// get the date from one week ago
		$one_week_ago = date("Y-m-d", strtotime("-1 week"));
		
		$query = file_get_contents("query.sql");
		$query = str_replace("%DATE%", $one_week_ago, $query);
		
		$result = pg_query($this->con, $query);
		while ($row = pg_fetch_row($result)) {
			$date_range = date("m/d/Y", strtotime("-1 week")) . "-" . date("m/d/Y", strtotime("now"));
			$company_name = $row[0];
			$count = $row[1];
			$this->text .= "$date_range,$company_name,$count\n";
		}
	}
}