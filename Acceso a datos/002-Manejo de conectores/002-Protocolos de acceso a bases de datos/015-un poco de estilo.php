<?php

if (isset($_POST['usuario'])) {
  $enlace = mysqli_connect(
    $_POST['servidor'],
    $_POST['usuario'],
    $_POST['contrasena'],
    $_POST['basededatos']
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
} else {
?>
  <!doctype html>
  <html>

  <head>
    <script src="https://cdn.tailwindcss.com"></script>
    <title>
      Instalador de bases de datos
    </title>
  </head>

  <body>
    <form method="POST" action="?" class="max-w-md mx-auto mt-10 p-6 bg-white rounded-lg shadow-md">
      <h1 class="text-2xl font-bold text-center mb-6">Instalador</h1>

      <div class="space-y-4">
        <input
          type="text"
          name="usuario"
          placeholder="Usuario de la base de datos"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent">

        <input
          type="text"
          name="contrasena"
          placeholder="Contraseña de la base de datos"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent">

        <input
          type="text"
          name="servidor"
          placeholder="Servidor de la base de datos"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent">

        <input
          type="text"
          name="basededatos"
          placeholder="Nombre de la base de datos"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent">
      </div>

      <button
        type="submit"
        class="w-full mt-6 px-4 py-2 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-600 transition duration-200">
        Instalar
      </button>
    </form>

  </body>

  </html>
<?php } ?>