let textos = document.querySelectorAll("textarea");

textos.forEach(function (textarea) {
  // creo el contenedor donde va el editor
  let nuevocontenedor = document.createElement("div");
  nuevocontenedor.className =
    "w-full max-w-xl mx-auto my-6 border border-gray-300 rounded shadow bg-white";

  // sustituyo el textarea por el contenedor y lo escondo
  textarea.replaceWith(nuevocontenedor);
  nuevocontenedor.appendChild(textarea);
  textarea.style.display = "none";

  // creo la barra de botones
  let botonera = document.createElement("div");
  botonera.className =
    "flex flex-wrap items-center gap-2 bg-gray-100 p-3 border-b border-gray-300 rounded-t";
  nuevocontenedor.appendChild(botonera);

  // funcion para crear botones de formato, le meto el html y la clase tailwind que quiero aplicar
  function crearBoton(html, claseTailwind) {
    let btn = document.createElement("button");
    btn.innerHTML = html;
    btn.className =
      "w-9 h-9 flex items-center justify-center border rounded hover:bg-gray-200";
    btn.onclick = function (e) {
      e.preventDefault(); // que no recargue ni haga cosas raras
      toggleTailwindClassInBlock(claseTailwind); // le meto o le quito la clase al bloque donde estoy escribiendo
    };
    botonera.appendChild(btn);
  }

  // botones que quiero que salgan
  crearBoton("<b>B</b>", "font-bold");
  crearBoton("<i>I</i>", "italic");
  crearBoton("<u>U</u>", "underline");
  crearBoton("<s>S</s>", "line-through");
  crearBoton("↑", "uppercase");

  // selector de color para el texto
  let colorfrente = document.createElement("input");
  colorfrente.type = "color";
  colorfrente.className = "w-9 h-9 p-1 border rounded";
  colorfrente.oninput = function () {
    aplicarColorEnBloque(colorfrente.value); // cambia el color del bloque
  };
  botonera.appendChild(colorfrente);

  // selector de tamaño de letra
  let tamaniofuente = document.createElement("select");
  tamaniofuente.className = "h-9 border rounded px-2 text-sm";
  [10, 12, 14, 16, 18, 20].forEach(function (t) {
    let opcion = document.createElement("option");
    opcion.textContent = t + "px";
    opcion.value = "text-[" + t + "px]";
    tamaniofuente.appendChild(opcion);
  });
  tamaniofuente.onchange = function () {
    aplicarClaseTextoEnBloque(tamaniofuente.value); // cambia el tamaño del texto del bloque
  };
  botonera.appendChild(tamaniofuente);

  // este es el editor donde escribo
  let mieditor = document.createElement("div");
  mieditor.className =
    "w-full min-h-[300px] p-4 border-t border-gray-300 text-sm rounded-b focus:outline-none";
  mieditor.setAttribute("contenteditable", "true");
  nuevocontenedor.appendChild(mieditor);

  // meto un div vacio para que no se escriba fuera de ningun bloque
  mieditor.innerHTML = "<div><br></div>";

  // cada vez que escribo, actualiza el textarea escondido
  mieditor.oninput = function () {
    textarea.value = mieditor.innerHTML;
  };

  // le mete o le quita una clase tailwind al bloque donde estoy escribiendo
  function toggleTailwindClassInBlock(claseTailwind) {
    let bloque = getBloqueActual();
    if (!bloque) return;
    bloque.classList.toggle(claseTailwind);
    textarea.value = mieditor.innerHTML;
  }

  // cambia el color del texto del bloque
  function aplicarColorEnBloque(color) {
    let bloque = getBloqueActual();
    if (!bloque) return;
    bloque.style.color = color;
    textarea.value = mieditor.innerHTML;
  }

  // cambia el tamaño del texto del bloque
  function aplicarClaseTextoEnBloque(claseNueva) {
    let bloque = getBloqueActual();
    if (!bloque) return;
    bloque.classList.forEach((c) => {
      if (c.startsWith("text-[")) bloque.classList.remove(c); // quito el tamaño anterior
    });
    bloque.classList.add(claseNueva);
    textarea.value = mieditor.innerHTML;
  }

  // esta funcion me dice en que bloque estoy escribiendo, div o p
  function getBloqueActual() {
    let selection = window.getSelection();
    if (!selection.rangeCount) return null;
    let node = selection.anchorNode;
    if (node.nodeType === 3) node = node.parentElement;
    while (node && node !== mieditor && !/^DIV|P$/.test(node.nodeName)) {
      node = node.parentElement;
    }
    return node && node !== mieditor ? node : null;
  }
});
