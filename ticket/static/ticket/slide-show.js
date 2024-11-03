// slideshow.js

let slideIndex = 0;
showSlides();

function showSlides() {
    let slides = document.getElementsByClassName("slide");
    let dots = document.getElementsByClassName("dot");
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) { slideIndex = 1 }
    for (let i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
    setTimeout(showSlides, 3000); // Change image every 3 seconds
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}

let images = ['1.jpg', 'image2.jpg', 'image3.jpg'];
let index = 0;
const container = document.querySelector('.slideshow-container');

function changeBackground() {
    container.style.backgroundImage = `url('${images[index]}')`;
    index = (index + 1) % images.length;
}

// Change background every 5 seconds
setInterval(changeBackground, 5000);

