var footer = document.querySelector('.footer');
if (document.documentElement.scrollHeight > window.innerHeight) {
    footer.classList.remove('fixed-position');
} else {
    footer.classList.add('fixed-position');
}