window.onload = function () {
  fetch("../../servidor/lista_tablas.php")
    .then((response) => {
      return response.json();
    })
    .then((datos) => {
      let menu = document.querySelector("nav ul");
      datos.forEach(function (tabla) {
        let nombre_de_la_tabla = tabla["Tables_in_crimson"];
        let elemento = document.createElement("li");
        elemento.textContent = nombre_de_la_tabla;
        elemento.onclick = function () {
          let texto = this.textContent;
          cargaDatosTabla(texto);
        };
        menu.appendChild(elemento);
      });
    });

  cargaDatosTabla("clientes");
};

function cargaDatosTabla(tabla) {
  fetch("../../servidor/columnas_tabla.php?tabla=" + tabla)
    .then((response) => {
      return response.json();
    })
    .then((datos) => {
      let cabeceras_tabla = document.querySelector("table thead tr");
      cabeceras_tabla.innerHTML = ""; // Limpiar el contenido previo
      datos.forEach(function (dato) {
        let elemento = document.createElement("th");
        elemento.textContent = dato["Field"];
        cabeceras_tabla.appendChild(elemento);
      });
    });

  fetch("../../servidor/datos_tabla.php?tabla=" + tabla)
    .then((response) => {
      return response.json();
    })
    .then((datos) => {
      let contenidoTabla = document.querySelector("section table tbody");
      contenidoTabla.innerHTML = ""; // Limpiar el contenido previo
      datos.forEach(function (registro) {
        console.log(registro);

        let nuevaFila = document.createElement("tr");
        Object.keys(registro).forEach((clave) => {
          let nuevaColumna = document.createElement("td");
          nuevaColumna.textContent = registro[clave];
          nuevaFila.appendChild(nuevaColumna);
        });
        contenidoTabla.appendChild(nuevaFila);
      });
    });
}
