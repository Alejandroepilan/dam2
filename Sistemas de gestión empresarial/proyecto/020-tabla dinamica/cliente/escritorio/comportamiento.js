window.onload = function () {
  fetch("../../servidor/lista_aplicaciones.php")
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      const plantilla = document.getElementById("plantilla_aplicacion");
      console.log(data);
      data.forEach(function (elemento) {
        console.log(elemento);
        const instancia = plantilla.content.cloneNode(true);
        const nombre = instancia.querySelector("p");
        nombre.innerHTML = elemento.nombre;
        const imagen = instancia.querySelector("img");
        imagen.setAttribute("src", "img/" + elemento.icono);
        document.querySelector("main").appendChild(instancia);
      });

      let aplicaciones = document.querySelectorAll(".aplicacion");
      aplicaciones.forEach(function (aplicacion) {
        aplicacion.onclick = function () {
          window.location = "../supercontrolador/";
        };
      });
    });
};
