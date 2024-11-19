var lienzo = document.querySelector("#lienzo1");
var contexto = lienzo.getContext("2d");
lienzo.width = 512;
lienzo.height = 512;

var lienzo2 = document.querySelector("#lienzo2");
var contexto2 = lienzo2.getContext("2d");
lienzo2.width = 512;
lienzo2.height = 512;
contexto2.fillStyle = "green";

var lienzoNivel = document.querySelector("#lienzoNivel");
var contextoNivel = lienzoNivel.getContext("2d");
lienzoNivel.width = 512;
lienzoNivel.height = 512;
contextoNivel.fillStyle = "green";

var lienzoFondo = document.querySelector("#lienzoFondo");
var contextoFondo = lienzoFondo.getContext("2d");
lienzoFondo.width = 512;
lienzoFondo.height = 512;
contextoFondo.fillStyle = "green";
