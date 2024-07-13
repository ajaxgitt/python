document.addEventListener('DOMContentLoaded', function () {
    const dropArea = document.querySelector('.drop-area')
    const dragText = document.querySelector('h2')
    const inputFile = document.getElementById('input-file')
    const preview = document.getElementById('preview')
    const uploadForm = document.getElementById('upload-form')

    dropArea.addEventListener('dragover', (event) => {
        event.preventDefault();
        dropArea.classList.add('dragover')
        dropArea.classList.add('active')
        dragText.textContent = 'Suelta para subir los archivos'
    });

    dropArea.addEventListener('dragleave', (e) => {
        e.preventDefault()
        dropArea.classList.remove('dragover')
        dropArea.classList.remove('active')
        dragText.textContent = 'Arrastra y suelta las imagenes'
    });

    dropArea.addEventListener('drop', (event) => {
        event.preventDefault()
        dropArea.classList.remove('dragover')
        inputFile.files = event.dataTransfer.files
        updatePreview()
    });

    inputFile.addEventListener('change', updatePreview)

    function updatePreview() {
        preview.innerHTML = ''
        const files = inputFile.files
        if (files.length === 0) {
            preview.innerHTML = '<p>No hay archivos seleccionados</p>'
        } else {
            Array.from(files).forEach(file => {
                const img = document.createElement('img')
                img.src = URL.createObjectURL(file)
                img.height = 100
                preview.appendChild(img)
            })
        }
    }

    uploadForm.addEventListener('submit', function (event) {
        event.preventDefault();

        if (inputFile.files.length === 0) {
            Swal.fire({
                icon: "error",
                title: "Por favor selecciona al menos una imagen.",
            });
            
            return;
        }

        const formData = new FormData(uploadForm);
        for (const file of inputFile.files) {
            formData.append('imagenes', file)
        }

        fetch(uploadForm.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    Swal.fire({
                        title: data.message,
                        icon: "success"
                        });
                    
                    preview.innerHTML = ''
                    inputFile.value = ''
                } else {
                    Swal.fire({
                        icon: "error",
                        title: data.message,
                    });
                }
            })
            .catch(error => {
                console.error('Error:', error)
                alert('Error subiendo las imágenes')
            })
    })
})
