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
}
