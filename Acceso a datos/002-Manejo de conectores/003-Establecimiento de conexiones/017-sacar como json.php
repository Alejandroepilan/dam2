<?php

$mysqli = mysqli_connect("localhost", "root", "", "accesoadatos");
$query = "SELECT * FROM empleados";
$result = mysqli_query($mysqli, $query);
$resultado = [];
while ($row = mysqli_fetch_assoc($result)) {
  $resultado[] = $row;
}
var_dump($resultado);
