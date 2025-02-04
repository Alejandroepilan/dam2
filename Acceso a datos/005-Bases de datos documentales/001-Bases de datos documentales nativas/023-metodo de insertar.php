<?php

class ConectaMongo
{
  private $servidor;
  private $basededatos;
  private $conexion;

  public function __construct()
  {
    $this->servidor = "mongodb://localhost:27017";
    $this->basededatos = "empresa";
    $this->conexion = new MongoDB\Driver\Manager($this->servidor);
  }

  public function listar($coleccion)
  {
    $query = new MongoDB\Driver\Query([]);
    $namespace = $this->basededatos . "." . $coleccion;
    $cursor = $this->conexion->executeQuery($namespace, $query);
    $resultado = [];
    foreach ($cursor as $document) {
      $resultado[] = $document;
    }
    $json = json_encode($resultado, JSON_PRETTY_PRINT);
    return $json;
  }

  public function insertar($coleccion, $datos)
  {
    $namespace = $this->basededatos . "." . $coleccion;
    $bulk = new MongoDB\Driver\BulkWrite;
    $bulk->insert($datos);
    $this->conexion->executeBulkWrite($namespace, $bulk);
    $query = new MongoDB\Driver\Query([]);
    $cursor = $this->conexion->executeQuery($namespace, $query);

    return 0;
  }
}

$conexion = new ConectaMongo();

$documento = [
  'nombre' => 'Juan',
  'email' => 'juan@gmail.com',
  'edad' => 30
];

$conexion->insertar("clientes", $documento);
