//ACT1
let afegir_text_v = document.getElementById("afegir-verd");
let afegir_rotacio = document.getElementById("afegir-rotacio");
let afegir_marge = document.getElementById("afegir-marge");
let afegir_borda = document.getElementById("afegir-borda");
let reset_afegir = document.getElementById("reset-afegir");
let caja = document.getElementById("caixa-afegir");

afegir_text_v.addEventListener("click", () => {
  caja.classList.add("text-verd");
});
afegir_rotacio.addEventListener("click", () => {
  caja.classList.add("rotacio");
});
afegir_marge.addEventListener("click", () => {
  caja.classList.add("marge");
});
afegir_borda.addEventListener("click", () => {
  caja.classList.add("marge-radius");
});
reset_afegir.addEventListener("click", () => {
  caja.className = "";
  caja.classList.add("caixa-afegir");
});

//ACT2
let boton_toggle = document.getElementById("toggle-activa");
let cajaToggle = document.getElementById("caixa-toggle");

boton_toggle.addEventListener("click", () => {  
  cajaToggle.classList.toggle("activa");
  boton_toggle.textContent = cajaToggle.classList.contains("activa") ? "Treu CSS" : "Aplica CSS";
});

//ACT3
let caja_ciclical = document.getElementById("caixa-canvi-estat");
let boton_change = document.getElementById("boto-canvi-classe");
let boton_reset = document.getElementById("reset-ciclic");
let info =document.getElementById("info-ciclic");
let estado = 1;

boton_reset.addEventListener('click', ()=>{
  estado = 1;
  caja_ciclical.className = "";
  caja_ciclical.classList.add("estat-1")
  info.textContent = estado;
})
boton_change.addEventListener('click',()=>{  
  estado++;
  estado = (estado>4) ? 1 : estado;
  caja_ciclical.className = ""
  caja_ciclical.classList.add(`estat-${estado}`);
  info.textContent = estado;
})