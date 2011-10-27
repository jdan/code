<?php

error_reporting(E_ALL | E_STRICT);

include('Alert.php');
include('CompetitionReport.php');
include('class.args.php');

$c = new CompetitionReport(false);
$c->sendAlert();