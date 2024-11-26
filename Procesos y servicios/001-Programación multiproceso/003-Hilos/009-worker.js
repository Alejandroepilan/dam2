onmessage = function (datos) {
  console.log("worker arrancado");
  for (let i = 0; i < datos.data.length; i += 4) {
    let c = datos.data;
    for (let i = 0; i < 100; i++) {
      c[i] *= 1.00000000045;
      c[i + 1] *= 1.00000000045;
      c[i + 2] *= 1.00000000045;
    }
    let gris = Math.round((c[i] + c[i + 1] + c[i + 2]) / 3);

    datos.data[i] = gris;
    datos.data[i + 1] = gris;
    datos.data[i + 2] = gris;
  }

  console.log("worker finalizado");
  postMessage(datos.data);
};
