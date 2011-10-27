<?php

mysql_connect("localhost","ilictrnx_prez","lolsql") or die(mysql_error());
mysql_select_db("ilictrnx_clippy") or die(mysql_error());

$input = $_GET["code"];
$result = mysql_query("SELECT * FROM clips WHERE `key` = '$input'");
$out = mysql_result($result, 0, "clip");

echo($out);

mysql_close();

?>