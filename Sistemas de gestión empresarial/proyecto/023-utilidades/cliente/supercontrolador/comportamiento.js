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
  let compoclave;

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
        if (dato["Key"] == "PRI") {
          compoclave = dato["Field"];
        }
      });
      let elemento = document.createElement("th");
      cabeceras_tabla.appendChild(elemento);

      fetch("../../servidor/datos_tabla.php?tabla=" + tabla)
        .then((response) => {
          return response.json();
        })
        .then((datos) => {
          let contenidoTabla = document.querySelector("section table tbody");
          contenidoTabla.innerHTML = ""; // Limpiar el contenido previo
          let clave_primaria;
          datos.forEach(function (registro) {
            let nuevaFila = document.createElement("tr");
            Object.keys(registro).forEach((clave) => {
              if (clave == compoclave) {
                clave_primaria = registro[clave];
              }
              let nuevaColumna = document.createElement("td");
              nuevaColumna.textContent = registro[clave];
              nuevaFila.appendChild(nuevaColumna);
            });
            let nuevaColumna = document.createElement("td");
            nuevaColumna.textContent = "🗑️";
            nuevaColumna.setAttribute("claveprimaria", clave_primaria);
            nuevaFila.appendChild(nuevaColumna);
            nuevaColumna.onclick = function () {
              let identificador = this.getAttribute("claveprimaria");
              fetch(
                "../../servidor/eliminar_dato.php?tabla=" +
                  tabla +
                  "&id=" +
                  identificador
              );
              this.parentElement.remove(); // Eliminar la fila de la tabla
            };
            contenidoTabla.appendChild(nuevaFila);
          });
        });
    });
}
