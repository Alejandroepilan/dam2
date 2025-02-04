db.clientes.updateMany(
  {
    nombre: "Alejandro",
  },
  {
    $set: { nombre: "Paco" },
  }
);
