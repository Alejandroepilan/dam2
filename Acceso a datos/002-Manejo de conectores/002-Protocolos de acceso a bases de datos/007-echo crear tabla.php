<?php

$enlace = mysqli_connect(
  "localhost",
  "root",
  "",
  "accesoadatos"
) or die("error");

$json = file_get_contents("004-modelodedatos.json");
$datos = json_decode($json, true);
var_dump($datos);
echo "<br><br>";
foreach ($datos as $dato) {
  var_dump($dato);
  $nombredetabla = $dato['nombre'];
  $cadena = "CREATE TABLE " . $nombredetabla . " ( ";
  $cadena .= " ) ";
  echo $cadena;
  echo "<br><br>";
}
