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



