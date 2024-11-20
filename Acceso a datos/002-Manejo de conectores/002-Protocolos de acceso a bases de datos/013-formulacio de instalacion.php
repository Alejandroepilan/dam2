<?php

if (isset($_POST['usuario'])) {
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
}
?>
<!doctype html>
<html>

<head>
  <title>
    Instalador de bases de datos
  </title>
</head>

<body>
  <form method="POST" action="?">
    <input type="text" name="usuario" placeholder="Usuario de la base de datos">
    <input type="text" name="contrasena" placeholder="Contraseña de la base de datos">
    <input type="text" name="servidor" placeholder="Servidor de la base de datos">
    <input type="text" name="basededatos" placeholder="Nombre de la base de datos">
    <input type="submit">
  </form>
</body>

</html>