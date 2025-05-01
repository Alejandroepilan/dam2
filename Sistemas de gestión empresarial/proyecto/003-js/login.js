window.onload = function () {
  console.log("Javascript cargado");
  document.querySelector("#login").onclick = function () {
    console.log("hola");
    let usuario = document.querySelector("#usuario").value;
    let contrasena = document.querySelector("#contrasena").value;
    console.log(usuario, contrasena);
    let envio = { usuario: usuario, contrasena: contrasena };
    console.log(envio);
  };
};
