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
        menu.appendChild(elemento);
      });
    });
};
