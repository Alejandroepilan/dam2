<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = mysqli_connect("localhost", "root", "", "crimson");
$query = "
		SELECT 
			nombre,
			descripcion,
			icono
		FROM aplicaciones 
		WHERE activa = 1
	";
$result = mysqli_query($mysqli, $query);
$aplicaciones = [];
while ($row = mysqli_fetch_assoc($result)) {
	$aplicaciones[] = $row;
}
echo json_encode($aplicaciones);
