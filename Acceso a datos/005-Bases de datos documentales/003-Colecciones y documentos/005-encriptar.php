<?php

$contrasena = "Alejandro";
echo "La contraseña sin encriptar " . $contrasena . "<br>";
$encriptado = base64_encode($contrasena);
echo "La contraseña encriptada " . $encriptado . "<br>";
$desencriptado = base64_decode($encriptado);
echo "La contraseña desencriptada " . $desencriptado . "<br>";
