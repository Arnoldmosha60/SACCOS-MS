// app.js
document.getElementById('postFormData').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get form data
    const formData = new FormData(this);

    // Convert form data to JSON
    const jsonData = {};
    formData.forEach((value, key) => {
        jsonData[key] = value;
    });

    // Make a POST request to your API endpoint
    fetch('http://127.0.0.1:8000/user/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(jsonData),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // You can perform additional actions here
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle errors
    });
});
