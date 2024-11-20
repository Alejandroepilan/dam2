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
        $fila[$clave] = $valor;
      }
      $resultado[] = $fila;
    }
    $json = json_encode($resultado, JSON_PRETTY_PRINT);
    return $json;
  }

  public function listadoTablas()
  {
    $query = "SHOW TABLES;";
    $result = mysqli_query($this->conexion, $query);
    $resultado = [];
    while ($row = mysqli_fetch_assoc($result)) {
      //$resultado[] = $row;																			
      $fila = [];
      foreach ($row as $clave => $valor) {
        $fila[$clave] = $valor;
      }
      $resultado[] = $fila;
    }
    $json = json_encode($resultado, JSON_PRETTY_PRINT);
    return $json;
  }

  public function insertaTabla($tabla, $valores)
  {
    $campos = "";
    $datos = "";
    foreach ($valores as $clave => $valor) {
      $campos .= $clave . ",";
      $datos .= "'" . $valor . "',";
    }
    $campos = substr($campos, 0, -1);
    $datos = substr($datos, 0, -1);
    $query = "
      INSERT INTO " . $tabla . " 
      (" . $campos . ") 
      VALUES (" . $datos . ");
      ";
    $result = mysqli_query($this->conexion, $query);
    return 0;
  }

  public function actualizaTabla($tabla, $valores, $id)
  {
    $query = "
    UPDATE " . $tabla . " 
    SET
    ";
    foreach ($valores as $clave => $valor) {
      $query .= $clave . "='" . $valor . "', ";
    }
    $query = substr($query, 0, -2);
    $query .= "
    WHERE Identificador = " . $id . "
    ";
    $result = mysqli_query($this->conexion, $query);
    return "";
  }

  public function eliminaTabla($tabla, $id)
  {
    $query = "
    DELETE FROM " . $tabla . " 
    WHERE Identificador = " . $id . ";
    ";
    $result = mysqli_query($this->conexion, $query);
  }

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
/*
echo $conexion->seleccionaTabla("empleados");
echo "<br><br>";
echo $conexion->listadoTablas(); */
echo $conexion->eliminaTabla("clientes", '4');
