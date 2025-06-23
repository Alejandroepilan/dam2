onmessage = function (datos) {
  console.log("Hola soy el núcleo", datos.data);
  postMessage("ok soy el worker y vuelvo al proceso principal");
};
