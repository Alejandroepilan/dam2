class Jugador {
  constructor() {
    this.x = 256;
    this.y = 256;
    this.vy = 0;
    this.cayendo = true;
    this.direccion = "izquierda";
  }
  dibuja() {
    if (this.direccion == "derecha") {
      contexto2.drawImage(
        imagenJugador,
        0,
        0,
        31,
        47,
        this.x - desfase_global_x,
        this.y,
        31,
        47
      );
    } else {
      contexto2.drawImage(
        imagenJugador,
        31,
        0,
        31,
        47,
        this.x - desfase_global_x,
        this.y,
        31,
        47
      );
    }
  }
  mueve() {
    if (this.cayendo == true) {
      jugador.vy += gravedad;
      jugador.y += jugador.vy;
    }
    this.muere();
    this.colisionNivel();
  }
  muere() {
    if (this.y > 512) {
      window.location = window.location;
    }
  }
  colisionNivel() {
    let pixel = contextoNivel.getImageData(
      this.x - desfase_global_x,
      this.y + 31,
      1,
      1
    );
    if (pixel.data[3] > 0) {
      this.cayendo = false;
    } else {
      this.cayendo = true;
    }
  }
}
