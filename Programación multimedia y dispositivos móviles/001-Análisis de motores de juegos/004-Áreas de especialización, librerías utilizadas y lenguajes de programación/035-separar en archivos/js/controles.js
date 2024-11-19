document.onkeydown = function (e) {
  if (e.key == "ArrowUp" && jugador.cayendo == false) {
    jugador.y -= 5;
    jugador.vy = salto;
  }
  if (e.key == "ArrowDown") {
    jugador.y += 5;
  }
  if (e.key == "ArrowLeft") {
    jugador.x -= 5;
    jugador.direccion = "izquierda";
  }
  if (e.key == "ArrowRight") {
    jugador.x += 5;
    jugador.direccion = "derecha";
  }
  if (e.keyCode == 32) {
    balas.push(new Bala());
  }
};
