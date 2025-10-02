let first_image = document.getElementById("uno");
let second_image =document.getElementById("dos");
let third_image =document.getElementById("tres");

let boton = document.getElementById("boton");
let contador_text =document.getElementById("contador");
let contador_num = document.getElementById("contador").textContent.split("1")
let cont = 0;

boton.addEventListener('click', ()=>{    
    cont++;
    cont = (cont>2) ? 0 : cont;
    first_image.hidden = (cont===0) ? false :true;
    second_image.hidden = (cont===1) ? false :true;
    third_image.hidden = (cont===2) ? false :true;
    contador_text.textContent = contador_num[0] + (cont+1) + contador_num[1]
})