class Npc {
  // Funcion que se ejecuta cuando se instancia el objeto
  constructor() {
    this.x = Math.random() * 2048;
    this.y = Math.random() * 512;
    this.angulo = Math.random() * Math.PI * 2;
    this.vy = 0;
  } // Detectar colisiones y rebote
  rebota() {
    if (this.x < 0) {
      this.x = 0;
      this.angulo += Math.PI;
    }
    if (this.x > 512) {
      this.x = 512;
      this.angulo += Math.PI;
    }
    if (this.y < 0) {
      this.y = 10;
      this.angulo += Math.PI;
    }
    if (this.y > 512) {
      this.y = 512;
      this.angulo += Math.PI;
    }
  } // Este metodo define el movimiento del npc
  mueve() {
    this.x += Math.cos(this.angulo);
    this.y += Math.sin(this.angulo);
  } // Este dibuja el npc
  dibuja() {
    contexto.drawImage(imagenMalo, this.x - desfase_global_x, this.y, 43, 51); // Los dos numero del final es el tamaño de la imagen reducido 10 veces de su tamaño original
  }
}
