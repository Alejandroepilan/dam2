var temporizador = setTimeout("bucle()", 1000);

function bucle() {
  if (jugador.x + desfase_global_x > 400) {
    desfase_global_x += 2;
  }
  if (jugador.x + desfase_global_x < 120) {
    desfase_global_x -= 2;
  }

  contexto.clearRect(0, 0, 512, 512);
  contexto2.clearRect(0, 0, 512, 512);

  contextoNivel.clearRect(0, 0, 512, 512);
  contextoNivel.drawImage(imagenNivel, 0 - desfase_global_x, 0, 2048, 512);

  for (let i = 0; i < misnpcs.length; i++) {
    misnpcs[i].mueve();
    misnpcs[i].rebota();
    misnpcs[i].dibuja();
  }

  for (let i = 0; i < balas.length; i++) {
    balas[i].mueve();
    balas[i].dibuja();
  }

  // comprobar si una bala colisiona con un npc
  for (let i = 0; i < balas.length; i++) {
    for (let j = 0; j < misnpcs.length; j++) {
      if (
        calculateDistance(balas[i].x, balas[i].y, misnpcs[j].x, misnpcs[j].y) <
        20
      ) {
        misnpcs.splice(j, 1);
      }
    }
  }

  jugador.mueve();
  jugador.dibuja();

  // Con esta linea obtengo un array con los colores de un pixel
  var datos = contexto.getImageData(jugador.x, jugador.y, 1, 1).data;
  var alpha = datos[3]; // El indice 3 es la transparencia
  if (alpha == 255) {
    window.location = window.location; // Recargar pagina
  }
  clearTimeout(temporizador);
  temporizador = setTimeout("bucle()", 10);
}
