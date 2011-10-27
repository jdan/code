<?php

mysql_connect("localhost","ilictrnx_prez","lolsql") or die(mysql_error());
mysql_select_db("ilictrnx_clippy") or die(mysql_error());

$input = $_GET["val"];
$r = (string)rand(0, 99999);
str_pad($r, 5, "0", STR_PAD_LEFT);

$result = mysql_query("SELECT * FROM clips WHERE `key` = '$r'");
$out = mysql_result($result, 0, "clip");

while (strlen($out) != 0) {
    $r = (string)rand(0, 99999);
    str_pad($r, 5, "0", STR_PAD_LEFT);

    $result = mysql_query("SELECT * FROM clips WHERE `key` = '$r'");
    $out = mysql_result($result, 0, "clip");
}

mysql_query("INSERT INTO clips VALUES ('$out', '$input');

echo($out);

mysql_close();

?>