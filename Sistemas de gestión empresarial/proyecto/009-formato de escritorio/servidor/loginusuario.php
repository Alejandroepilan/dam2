<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = mysqli_connect("localhost", "root", "", "crimson");
$query = "
		SELECT 
		usuario
		FROM usuarios 
		WHERE usuario = '" . $_GET['usuario'] . "' 
		AND contrasena = '" . $_GET['contrasena'] . "'
	";
$result = mysqli_query($mysqli, $query);
if ($row = mysqli_fetch_assoc($result)) {
  $row['resultado'] = 'ok';
  echo json_encode($row);
} else {
  echo '{"resultado:":"ko"}';
}
