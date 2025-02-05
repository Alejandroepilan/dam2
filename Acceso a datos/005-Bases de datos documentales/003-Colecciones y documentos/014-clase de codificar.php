<?php
class EpilaCodifica
{

  public function codifica($entrada)
  {
    $salida = '';
    for ($i = 0; $i < strlen($entrada); $i++) {
      $salida .= chr(ord($entrada[$i]) + 5);
    }
    $salida = base64_encode(base64_encode(base64_encode($salida)));

    return $salida;
  }

  public function descodifica($entrada)
  {
    $entrada = base64_decode(base64_decode(base64_decode($entrada)));

    $salida = '';
    for ($i = 0; $i < strlen($entrada); $i++) {
      $salida .= chr(ord($entrada[$i]) - 5);
    }

    return $salida;
  }
}

// Ejemplo de uso
$codificador = new EpilaCodifica();

$textoOriginal = "Hola mundo!";
$textoCodificado = $codificador->codifica($textoOriginal);
echo "Texto codificado: $textoCodificado\n";
echo "</br>";
$textoDescodificado = $codificador->descodifica($textoCodificado);
echo "Texto descifrado: $textoDescodificado\n";
