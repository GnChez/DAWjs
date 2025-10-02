let tasca = document.getElementById("novaTasca");
let add_boton = document.getElementById("add");
let delete_boton = document.getElementById("delete");
let container = document.getElementById("container");
let contador = 1;
let tascas = [];

add_boton.addEventListener("click", () => {
  if (tasca.value === "") {
    alert("no n'hi ha tasques");
    return;
  }
  crearTasca();
});

delete_boton.addEventListener("click", () => {
  container.innerHTML = "";
  contador = 1;
});

tasca.addEventListener("keypress", (e) => {
  if (e.key == "Enter") {
    if (tasca.value === "") {
      alert("no n'hi ha tasques");
      return;
    }
    crearTasca();
  }
});

container.addEventListener("click", (event) => {
  if (event.target.classList.contains("boto-dlt")) {
    event.target.parentElement.remove();
  }

  console.log(event.target.parentElement.innerHTML.trim());
});

function crearTasca() {
  let newDiv = document.createElement("div");
  newDiv.className = contador % 2 == 0 ? "tasca-parell" : "tasca-imparell";
  let newH3 = document.createElement("h3");
  let textH3 = document.createTextNode(`Tasca ${contador}`);
  newH3.appendChild(textH3);
  let newP = document.createElement("p");
  let textP = document.createTextNode(`${tasca.value}`);
  newP.appendChild(textP);

  newDiv.appendChild(newH3);
  newDiv.appendChild(newP);
  let newBoton = document.createElement("button");
  let textButton = document.createTextNode("Borrar");
  newBoton.classList.add("boto-dlt");
  newBoton.appendChild(textButton);
  newDiv.appendChild(newBoton);
  container.insertAdjacentElement("beforeend", newDiv);
  tasca.value = "";
  contador++;
}
