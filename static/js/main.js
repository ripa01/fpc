// Get elements from the DOM
const menuBtn = document.querySelector('.menu-btn');
const menu = document.querySelector('.menu-container');
const dropdowns = document.querySelectorAll('.dropdown > div');
searchToggle = document.querySelector(".searchToggle");

// Toggle variable
let menuOpen = false;

// Set click event to menu button
menuBtn.addEventListener('click', () => {
    // Toggle mega menu show class
    menu.classList.toggle('mega-menu-show');
    // If the menu open variable is false
    if (menuOpen === false) {
        // Set the close icon to the menu button
        menuBtn.innerHTML = `
        <span class="material-symbols-outlined">
            close
        </span>
        `;
        // Set menu open to true
        menuOpen = true;
    }
    else {
        // Set the menu icon to the menu button
        menuBtn.innerHTML = `
        <span class="material-symbols-outlined">
            menu
        </span>
        `;
        // Set menu open to false
        menuOpen = false;
    }
});

// Select all dropdowns
dropdowns.forEach(dropdown => {
    // Add click event
    dropdown.addEventListener("click", (e) => {
        // Toggle dropdown menu show class
        dropdown.nextElementSibling.classList.toggle('menu-show');
        // Toggle icon rotated class
        dropdown.lastElementChild.classList.toggle('icon-rotated');
    });
});


// js code to toggle search box
searchToggle.addEventListener("click", () => {
    searchToggle.classList.toggle("active");
});


$(document).ready(function () {
    var yearElement = document.querySelector("#year");
    if (yearElement) {
        yearElement.innerText = new Date().getFullYear();
    } else {
        console.error("Element with id 'year' not found.");
    }
});


// disabling inspect element
// document.addEventListener("contextmenu", function (e) {
//     e.preventDefault(); //this prevents right click
// });
// document.onkeydown = function (e) {
//     if (event.keycode == 123) {
//         return false;
//     }
//     if (e.ctrlKey && e.shiftKey && e.keyCode == "I".charCodeAt(0)) {
//         return false;
//     }
//     if (e.ctrlKey && e.shiftKey && e.keyCode == "C".charCodeAt(0)) {
//         return false;
//     }
//     if (e.ctrlKey && e.shiftKey && e.keyCode == "J".charCodeAt(0)) {
//         return false;
//     }
//     if (e.ctrlKey && e.keyCode == "U".charCodeAt(0)) {
//         return false;
//     }
//     if (e.ctrlKey && e.keyCode == "S".charCodeAt(0)) {
//         return false;
//     }
// };

//step 1: get DOM
let nextDom = document.getElementById('next');
let prevDom = document.getElementById('prev');

let carouselDom = document.querySelector('.carousel');
let SliderDom = carouselDom.querySelector('.carousel .list');
let thumbnailBorderDom = document.querySelector('.carousel .thumbnail');
let thumbnailItemsDom = thumbnailBorderDom.querySelectorAll('.item');
let timeDom = document.querySelector('.carousel .time');

thumbnailBorderDom.appendChild(thumbnailItemsDom[0]);
let timeRunning = 3000;
let timeAutoNext = 7000;

nextDom.onclick = function(){
    showSlider('next');    
}

prevDom.onclick = function(){
    showSlider('prev');    
}
let runTimeOut;
let runNextAuto = setTimeout(() => {
    next.click();
}, timeAutoNext)
function showSlider(type){
    let  SliderItemsDom = SliderDom.querySelectorAll('.carousel .list .item');
    let thumbnailItemsDom = document.querySelectorAll('.carousel .thumbnail .item');
    
    if(type === 'next'){
        SliderDom.appendChild(SliderItemsDom[0]);
        thumbnailBorderDom.appendChild(thumbnailItemsDom[0]);
        carouselDom.classList.add('next');
    }else{
        SliderDom.prepend(SliderItemsDom[SliderItemsDom.length - 1]);
        thumbnailBorderDom.prepend(thumbnailItemsDom[thumbnailItemsDom.length - 1]);
        carouselDom.classList.add('prev');
    }
    clearTimeout(runTimeOut);
    runTimeOut = setTimeout(() => {
        carouselDom.classList.remove('next');
        carouselDom.classList.remove('prev');
    }, timeRunning);

    clearTimeout(runNextAuto);
    runNextAuto = setTimeout(() => {
        next.click();
    }, timeAutoNext)
}


