onmessage = function (datos) {
  console.log("worker arrancado");

  for (let i = 0; i < datos.data.length; i += 4) {
    if (datos.data[i] < 100) {
      datos.data[i] = 0;
      datos.data[i + 1] = 0;
      datos.data[i + 2] = 0;
    } else {
      datos.data[i] = 255;
      datos.data[i + 1] = 255;
      datos.data[i + 2] = 255;
    }
  }

  console.log("worker finalizado");
  postMessage(datos.data);
};
