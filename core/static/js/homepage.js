const hamburger = document.querySelector(".hamburger"); 
const navbar = document.querySelector('.navbar')
const line1 = document.querySelector('#line-1')
const line2 = document.querySelector('#line-2')
const line3 = document.querySelector('#line-3')
const navLinks = document.querySelectorAll('.nav-link')

const toggleNavBar = () => {
    if (window.innerWidth <= 1000) {
        navbar.classList.toggle('open')
        line1.classList.toggle('left-rotate')
        line2.classList.toggle('right-rotate')
        line3.classList.toggle('d-none')
    }
}
hamburger.addEventListener('click', () => { toggleNavBar() })
navLinks.forEach(link => { link.addEventListener('click', () => { toggleNavBar() }) })
window.addEventListener("scroll", () => {
    const nav = document.querySelector("nav")
    const scrollPos = window.scrollY
    nav.classList.toggle('scrolled', scrollPos > nav.offsetHeight)
})

