const dropdownBtn = document.querySelector(".dropdown__btn")
const dropdownMenu = document.querySelector(".dropdown__menu")

dropdownBtn.addEventListener("click", () => {
    dropdownMenu.classList.toggle("hide");

})  
  

// function showRight() {
//     var rightWindow = document.getElementById("rightWindow");
//     var leftWindow = document.getElementById("leftWindow");
//     if (rightWindow.style.width === "75%") {
//         // rightWindow.style.display = "block";
//         rightWindow.style.width = "0%";
//     } else {
//     //   rightWindow.style.display = "none";
//       rightWindow.style.width = "75%";
//     }
// }