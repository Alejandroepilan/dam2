<?php
$myfile = fopen("resultados.txt", "a");
$txt = $_GET['resultado'] . "\n";
fwrite($myfile, $txt);
fclose($myfile);
