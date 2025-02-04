db.clientes.insertOne({
  nombre: "Alejandro",
  apellidos: "Epila",
  correos: [
    { tipo: "personal", correo: "email1@gmal.com" },
    { tipo: "trabajo", correo: "email2@gmal.com" },
  ],
});
