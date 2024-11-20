<?php
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
    $this->usuario = "crimson";
    $this->contrasena = "crimson";
    $this->basededatos = "crimson";

    $this->conexion = mysqli_connect(
      $this->servidor,
      $this->usuario,
      $this->contrasena,
      $this->basededatos
    );
  }
  public function seleccionaTabla($tabla)
  {
    $query = "SELECT * FROM information_schema.key_column_usage
    WHERE table_name = '" . $tabla . "' AND REFERENCED_TABLE_NAME IS NOT NULL;";

    $result = mysqli_query($this->conexion, $query);
    $restricciones = [];
    while ($row = mysqli_fetch_assoc($result)) {
      $restricciones[] = $row;
    }

    $query = "SELECT * FROM " . $tabla . ";";
    $result = mysqli_query($this->conexion, $query);
    $resultado = [];
    while ($row = mysqli_fetch_assoc($result)) {

      $fila = [];
      foreach ($row as $clave => $valor) {
        $pasas = true;
        foreach ($restricciones as $restriccion) {
          if ($clave == $restriccion["COLUMN_NAME"]) {
            $query2 = "SELECT * FROM " . $restriccion["REFERENCED_TABLE_NAME"] . ";";
            $result2 = mysqli_query($this->conexion, $query2);
            $cadena = "";
            while ($row2 = mysqli_fetch_assoc($result2)) {
              foreach ($row2 as $campo) {
                $cadena .= $campo . "-";
              }
            }

            $fila[$clave] = $cadena;
            $pasas = false;
          }
        }
        if ($pasas == true) {
          $fila[$clave] = $valor;
        }
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
