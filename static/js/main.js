console.log("%cHello fellow developers! I'm a software engineer with over 10 years experience. I'm always ready for a new challenge. If you're looking to collaborate on a project, send me a message. You'll find my contact information on this page. Looking forward to hearing from you.",'background: #222; color: #bada55; padding:15px;border-radius:10px;')

$('#loader').hide()
$('a').on('click',({currentTarget})=>{
  
    if(currentTarget.href.includes('#') && !window.location.href.includes('#')){
        $('#loader').show()
    }
})
$('button').on('click',()=>{
        $('#loader').show()    
})

$('form').on('submit',()=>{
    $('#loader').show()
})

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
