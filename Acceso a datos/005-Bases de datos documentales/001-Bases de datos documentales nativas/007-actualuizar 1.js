db.clientes.updateOne(
  {
    nombre: "Alejandro",
  },
  {
    $set: { nombre: "Paco" },
  }
);
