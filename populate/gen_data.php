<?php

	$interestType = $_POST['interestType'];
	$txtWeight = $_POST['txtWeight'];
	$command = 'sudo python3 /var/www/html/back_end.py $interestType $txtWeight';
	$output = passthru($comand);

	header('Location: index.php');
?>
