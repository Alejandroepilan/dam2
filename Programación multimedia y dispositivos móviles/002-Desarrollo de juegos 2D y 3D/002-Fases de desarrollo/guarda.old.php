<?php
$myfile = fopen("tablero.html", "w") or die("No");
$txt = $_GET['datos'];
fwrite($myfile, $txt);
fclose($myfile);
