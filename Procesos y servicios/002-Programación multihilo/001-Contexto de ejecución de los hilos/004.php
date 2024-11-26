<?php
$file = 'tareas.txt';

$lines = file($file);

echo $lines[0];

array_shift($lines);

file_put_contents($file, implode('', $lines));
