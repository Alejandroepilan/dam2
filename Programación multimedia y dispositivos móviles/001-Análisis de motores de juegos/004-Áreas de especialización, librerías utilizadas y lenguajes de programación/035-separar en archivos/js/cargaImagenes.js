var imagenJugador = new Image();
imagenJugador.src = "./img/spriteJugador.png";

var imagenMalo = new Image();
imagenMalo.src = "./img/malo.png";

var imagenFondo = new Image();
imagenFondo.src = "./img/fondo.png";
imagenFondo.onload = function () {
  contextoFondo.drawImage(imagenFondo, 0, 0);
};

var imagenNivel = new Image();
imagenNivel.src = "./img/nivel1.png";
imagenNivel.onload = function () {
  contextoNivel.imageSmoothingEnabled = false;
  contextoNivel.drawImage(imagenNivel, 0, 0, 2048, 512);
};
