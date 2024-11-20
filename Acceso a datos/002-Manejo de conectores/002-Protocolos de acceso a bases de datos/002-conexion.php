<?php

$enlace = mysqli_connect(
  "localhost",
  "root",
  "",
  "accesoadatos"
) or die("error");

mysqli_query($link, "
  CREATE TABLE clientes (
    nombre VARCHAR(100),
    apellidos VARCHAR(100)
  );");
