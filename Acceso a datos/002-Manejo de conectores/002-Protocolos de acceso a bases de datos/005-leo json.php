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
