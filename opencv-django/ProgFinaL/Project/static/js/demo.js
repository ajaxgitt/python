document.addEventListener('DOMContentLoaded', (event) => {
    const comenzar = document.getElementById('iniciar')
    const empezar = document.getElementById('video-stream')

    comenzar.addEventListener('click', (e) => {
        e.preventDefault()
        empezar.src = enlace
        comenzar.classList.toggle('active')
    })

})



document.addEventListener('DOMContentLoaded', (event) => {
    const finalizar = document.getElementById('fin')

    finalizar.addEventListener('click', (e) => {
        e.preventDefault()
        Swal.fire({
            title: '¿Estás seguro?',
            text: "¿Quieres salir de la  demostracion?",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, salir',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
                window.location.href = salir;
            }
        })
    })
})

