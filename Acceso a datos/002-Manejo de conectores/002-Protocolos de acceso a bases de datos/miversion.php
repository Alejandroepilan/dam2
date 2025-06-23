<?php
mysqli_report(MYSQLI_REPORT_OFF); // Desactiva las errores en pantalla
$mensajes = []; // array para almacenar mensajes de ok o error
$enlace = false; // Variable para almacenar estado de la conexion

if (isset($_POST['usuario'])) {
  $enlace = @mysqli_connect( // El @ desactiva los errores en pantalla
    $_POST['servidor'],
    $_POST['usuario'],
    $_POST['contrasena'],
    $_POST['basededatos']
  ); // Aqui devuelve true

  // Si es false envia el error, si es true continua
  if (!$enlace) {
    $mensajes[] = ['error', "❌ Error de conexión: " . mysqli_connect_error()];
  } else {

    $json = file_get_contents("004-modelodedatos.json");
    $datos = json_decode($json, true);

    foreach ($datos as $dato) {
      $nombredetabla = $dato['nombre'];

      // Comprobar si la tabla ya existe
      $existe = mysqli_query($enlace, "SHOW TABLES LIKE '$nombredetabla'");
      if (mysqli_num_rows($existe) > 0) {
        $mensajes[] = ['error', "❌ La tabla <strong>$nombredetabla</strong> ya existe."];
        continue;
      }

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

      // Ejecutar
      if (mysqli_query($enlace, $cadena)) {
        $mensajes[] = ['ok', "✅ Tabla <strong>$nombredetabla</strong> creada correctamente."];
      } else {
        $mensajes[] = ['error', "❌ Error creando la tabla <strong>$nombredetabla</strong>: " . mysqli_error($enlace)];
      }
    }
  }
}
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
  <form method="POST" class="max-w-md mx-auto mt-10 p-6 bg-white rounded-lg shadow-md">
    <h1 class="text-2xl font-bold text-center mb-6">Instalador de bases de datos</h1>

    <div class="space-y-4">
      <input
        type="text"
        name="usuario"
        value="<?php echo $_POST['usuario'] ?? '' ?>"
        placeholder="Usuario"
        class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent">

      <input
        type="password"
        name="contrasena"
        placeholder="Contraseña"
        class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent">

      <input
        type="text"
        name="servidor"
        value="<?php echo $_POST['servidor'] ?? '' ?>"
        placeholder="Servidor"
        class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent">

      <input
        type="text"
        name="basededatos"
        value="<?php echo $_POST['basededatos'] ?? '' ?>"
        placeholder="Nombre"
        class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent">
    </div>

    <button
      type="submit"
      class="w-full mt-6 px-4 py-2 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-600 transition duration-200">
      Instalar
    </button>

    <?php if (!empty($mensajes)): // Cuadro para mostrar mensajes de ok y error 
    ?>
      <div class="mt-6 space-y-2">
        <?php foreach ($mensajes as $msg): ?>
          <div class="p-3 rounded <?php echo $msg[0] === 'ok' ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'; ?>">
            <?php echo $msg[1]; ?>
          </div>
        <?php endforeach; ?>
      </div>
    <?php endif; ?>
  </form>

</body>

</html>