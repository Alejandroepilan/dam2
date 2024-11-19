var gravedad = 1;
var salto = -16;

var desfase_global_x = 0;

var jugador = new Jugador(); // Aqui instacion 1 jugador
var misnpcs = []; // Aqui instancio los npc en un array de 50 elementos
var balas = [];
var numeronpc = 5;
for (let i = 0; i < numeronpc; i++) {
  misnpcs[i] = new Npc();
}
