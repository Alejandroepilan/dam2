<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

include "conexionDB.php";

$conexion = new conexionDB();

$json = $conexion->seleccionaTabla("lineaspedido");
$datos = json_decode($json, true);

//echo $json;
?>

<!DOCTYPE html>
<html lang="es">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com"></script>
  <title>Visor tablas SQL</title>
</head>

<body class="bg-gray-100 p-6">
  <div class="max-w-7xl mx-auto bg-white p-6 rounded shadow">
    <table class="table-auto w-full border border-gray-300">
      <thead class="bg-gray-200">
        <tr>
          <?php foreach ($datos[0] as $columna => $valor): ?>
            <th class="border px-4 py-2 text-left"><?php echo $columna; ?></th>
          <?php endforeach; ?>
        </tr>
      </thead>
      <tbody>
        <?php foreach ($datos as $fila): ?>
          <tr class="hover:bg-gray-100">
            <?php foreach ($fila as $valor): ?>
              <td class="border px-4 py-2"><?php echo $valor; ?></td>
            <?php endforeach; ?>
          </tr>
        <?php endforeach; ?>
      </tbody>
    </table>
  </div>
</body>

</html>