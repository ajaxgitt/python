let menu = document.querySelector('#menu-ico')
let navbar = document.querySelector('.navbar')

menu.onclick=()=>{
    menu.classList.toggle('fa-xmark')
    navbar.classList.toggle('active')
}


let sections = document.querySelectorAll('section')
let navLinks = document.querySelectorAll('header nav a')

window.onscroll = ()=>{
    sections.forEach(sec =>{
        let top = window.screenY
        let offset = sec.offsetTop -150
        let height = sec.offsetHeight
        let id = sec.getAttribute('id')

        if(top >= offset && top < offset + height){
            navLinks.forEach.apply(links => {
                links.classList.remove('active')
                document.querySelector('header nav a[href*="'+ id +'"]').classList.add('active'); // Corregir la selección de enlace
                //document.querySelector('header nav a [href*='+id+']').classList.add('active')
            })
        }
    })
    
    let header = document.querySelector('header')
    header.classList.toggle('sticky', window.scrollY>100)

    menu.classList.remove('fa-xmark')
    navbar.classList.remove('active')
}

ScrollReveal({
    distace:'80px',
    duration: 2000,
    delay:200,
})

ScrollReveal().reveal('.home-content, heading', { origin: 'top' })
ScrollReveal().reveal('.home-img, .services-container, .portafolio-box', { origin: 'buttom' });
ScrollReveal().reveal('.about-content', { origin: 'top' })
ScrollReveal().reveal('.about .heading', { origin: 'left' })

var typed = new Typed(('.multiple-text'),{
    strings : ['Reconocimiento facial avanzado', 'Reconocimiento facial avanzado','Reconocimiento facial avanzado'],
    typedSpeed :70,
    backSpeed :70,
    backDelay : 1000,
    loop : true
})

