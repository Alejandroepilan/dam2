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
    $this->conexion = new MongoDB\Driver\Manager($servidor);
  }

  public function listar($coleccion)
  {
    $query = new MongoDB\Driver\Query([]);
    $namespace = $this->basededatos . "." . $coleccion;
    $cursor = $manager->executeQuery($namespace, $query);
    $resultado = [];
    foreach ($cursor as $document) {
      $resultado[] = $document;
    }
    $json = json_encode($resultado, JSON_PRETTY_PRINT);
    return $json;
  }
}
