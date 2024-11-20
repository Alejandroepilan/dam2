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
  $cadena = "CREATE TABLE " . $nombredetabla . " ( Identificador INT NOT NULL AUTO_INCREMENT , ";
  foreach ($dato['columnas'] as $columna) {
    $cadena .= $columna['nombre'] . " " . $columna['tipo'] . " ";
    if ($columna['tipo'] != "TEXT") {
      $cadena .= " (" . $columna['longitud'] . ") ";
    }
    $cadena .= ",";
  }
  $cadena .= "PRIMARY KEY (Identificador) ";
  $cadena .= " )  ENGINE = InnoDB";
  mysqli_query($enlace, $cadena);
}
