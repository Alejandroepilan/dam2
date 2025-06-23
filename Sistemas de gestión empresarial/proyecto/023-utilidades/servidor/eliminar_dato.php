<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = mysqli_connect("localhost", "root", "", "crimson");
$query = "
		DELETE FROM " . $_GET['tabla'] . " WHERE Identificador = " . $_GET['id'] . ";
	";
$result = mysqli_query($mysqli, $query);
$aplicaciones = [];
while ($row = mysqli_fetch_assoc($result)) {
  $aplicaciones[] = $row;
}
echo json_encode($aplicaciones);
