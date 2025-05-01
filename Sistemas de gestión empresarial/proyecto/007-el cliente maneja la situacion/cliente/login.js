window.onload = function () {
  console.log("Javascript cargado");
  document.querySelector("#login").onclick = function () {
    console.log("hola");
    let usuario = document.querySelector("#usuario").value;
    let contrasena = document.querySelector("#contrasena").value;
    console.log(usuario, contrasena);
    let envio = { usuario: usuario, contrasena: contrasena };
    console.log(envio);

    fetch(
      "../servidor/loginusuario.php?usuario=" +
        usuario +
        "&contrasena=" +
        contrasena
    )
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        console.log(data);

        if (data.resultado == "ok") {
          console.log("Login correcto");
          localStorage.setItem("crimson_usuario", data.usuario);
        } else {
          console.log("Login incorrecto");
          document.querySelector("#feedback").innerHTML =
            "Usuario o contraseña incorrectos. Redirigiendo...";
          setTimeout(() => {
            window.location = window.location;
          }, 5000);
        }
      });
  };
};
