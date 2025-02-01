document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();
    let formData = new FormData(this);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            alert('Scan Results: ' + JSON.stringify(data.matches));
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});


