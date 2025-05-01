window.onload = function () {
  fetch("../../servidor/lista_aplicaciones.php")
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log(data);
    });
};
