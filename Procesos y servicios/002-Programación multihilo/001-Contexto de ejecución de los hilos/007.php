<?php
$file = 'tareas.txt';

$lines = file($file);
$tarea = $lines[0];

echo $lines[0];

array_shift($lines);

file_put_contents($file, implode('', $lines));

$myfile = fopen("asignaciones.txt", "a");
$txt = "Al usuario " . $_GET['usuario'] . " le ha tocado la tarea: " . $tarea . "\n";
fwrite($myfile, $txt);
fclose($myfile);
