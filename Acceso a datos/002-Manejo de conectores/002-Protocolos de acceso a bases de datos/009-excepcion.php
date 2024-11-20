<?php

$enlace = mysqli_connect(
  "localhost",
  "root",
  "",
  "accesoadatos"
) or die("error");

$json = file_get_contents("004-modelodedatos.json");
$datos = json_decode($json, true);

foreach ($datos as $dato) {
  $nombredetabla = $dato['nombre'];
  $cadena = "CREATE TABLE " . $nombredetabla . " ( ";
  foreach ($dato['columnas'] as $columna) {
    $cadena .= $columna['nombre'] . " " . $columna['tipo'] . " ";
    if ($columna['tipo'] != "TEXT") {
      $cadena .= " (" . $columna['longitud'] . ") ";
    }
    $cadena .= ",";
  }
  $cadena = substr($cadena, 0, -1);
  $cadena .= " ) ";
  mysqli_query($enlace, $cadena);
}
