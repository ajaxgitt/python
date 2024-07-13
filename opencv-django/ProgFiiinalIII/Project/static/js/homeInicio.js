document.addEventListener('DOMContentLoaded', (event) => {
    const comenzar = document.getElementById('iniciar')
    const empezar = document.getElementById('video-stream')

    comenzar.addEventListener('click', (e) => {
        console.log('se iso click en comenzar')
        e.preventDefault()
        empezar.src = enlace
        comenzar.classList.toggle('active')
    })

})

let endOfStreamDetected = false

function handleStreamEnd() {
    if (!endOfStreamDetected) {
        const comenzar = document.getElementById('iniciar')
        const comenzar2 = document.getElementById('inicir')
        console.log('handleStreamEnd called')
        const videoStream = document.getElementById('video-stream')
        videoStream.src = enlace2
        comenzar.classList.toggle('success')

        const message = document.createElement('p')
        message.innerText = "la recopilacion de datos fue un exito!"
        videoStream.parentNode.appendChild(message)


        setTimeout(function () {
            comenzar.classList.add('adf');
        }, 2000);


        setTimeout(function () {
            comenzar2.classList.remove('adf');
        }, 2000);


        
    }
}


const videoStream = document.getElementById('video-stream')
videoStream.addEventListener('load', function () {
    fetch(videoStream.src)
        .then(response => response.text())
        .then(text => {
            if (text.includes('END_OF_STREAM')) {
                console.log('se recivio el mensaje final')
                handleStreamEnd();
            }
        })
        .catch(error => {
            console.error('Error fetching the stream:', error)
        });
})

