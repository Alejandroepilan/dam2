<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

class conexionDB
{

  private $servidor;
  private $usuario;
  private $contrasena;
  private $basededatos;
  private $conexion;

  public function __construct()
  {
    $this->servidor = "localhost";
    $this->usuario = "root";
    $this->contrasena = "";
    $this->basededatos = "accesoadatos";

    $this->conexion = mysqli_connect(
      $this->servidor,
      $this->usuario,
      $this->contrasena,
      $this->basededatos
    );
  }
  public function seleccionaTabla($tabla)
  {
    $query = "SELECT * FROM " . $tabla . ";";
    $result = mysqli_query($this->conexion, $query);
    $resultado = [];
    while ($row = mysqli_fetch_assoc($result)) {
      //$resultado[] = $row;											// Los añado al array
      $fila = [];
      foreach ($row as $clave => $valor) {
        $fila[$clave] = $this->codifica($valor);
      }
      $resultado[] = $fila;
    }
    $json = json_encode($resultado, JSON_PRETTY_PRINT);
    return $json;
  }

  public function insertaTabla($tabla, $valores) {}

  public function actualizaTabla($tabla, $valores) {}

  public function eliminaTabla($tabla, $id) {}

  private function codifica($entrada)
  {
    return base64_encode($entrada);
  }

  private function decodifica($entrada)
  {
    return base64_decode($entrada);
  }
}

$conexion = new conexionDB();

echo $conexion->seleccionaTabla("empleados");
