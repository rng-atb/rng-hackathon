<?php

        $interestType = $_POST['interestType'];
        $txtWeight = $_POST['txtWeight'];
        $command = 'sudo /usr/bin/python3 /var/www/html/back_end.py ' . $intere$
        $output = shell_exec($command);
        header('Location: index.php');
?>
