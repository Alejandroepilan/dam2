class Bala {
  constructor() {
    this.x = jugador.x;
    this.y = jugador.y;
    this.vx = 10;
    if (jugador.direccion == "izquierda") {
      this.direccion = -1;
    } else {
      this.direccion = 1;
    }
  }
  mueve() {
    this.x += this.direccion * this.vx;
  }
  dibuja() {
    contexto.beginPath();
    contexto.arc(this.x - desfase_global_x, this.y, 10, 0, Math.PI * 2);
    contexto.fill();
  }
}
