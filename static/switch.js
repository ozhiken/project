const autoencrBtnr = document.querySelector(".autoencrBtnr");
const manualencrBtn = document.querySelector(".manualencrBtn");
const moveBtn = document.querySelector(".moveBtn");
const autoencr = document.querySelector(".autoencr");
const manualencr = document.querySelector(".manualencr");

manualencrBtn.addEventListener("click",()=>{
    moveBtn.classList.add("rightBtn");
    manualencr.classList.add("manualencrForm");
    autoencr.classList.remove("autoencrForm");
    moveBtn.innerHTML = "Manual";
})

autoencrBtnr.addEventListener("click",()=>{
    moveBtn.classList.remove("rightBtn");
    manualencr.classList.remove("manualencrForm");
    autoencr.classList.add("autoencrForm");
    moveBtn.innerHTML = "Auto-Generate";
})