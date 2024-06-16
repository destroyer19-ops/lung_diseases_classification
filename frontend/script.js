document.getElementById('uploadForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = new FormData();
    const fileField = document.getElementById('inputImage').files[0];

    formData.append('xray_image', fileField);

    try {
        const response = await fetch('http://127.0.0.1:5000/classify', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (response.ok) {
            document.getElementById('results').classList.remove('hidden'); // Assuming you have a hidden CSS class
            document.getElementById('imgName').textContent = fileField.name;
            document.getElementById('filename').textContent = fileField.name;
            // Update the rest of the results
            // Assuming `data` has keys 'classification', 'Normal', 'Tuberculosis', 'Covid', 'Lung_Opacity'
            document.getElementById('results').innerHTML += `
                <p>Classification: ${data.classification}</p>
                <p>Normal: ${data.Normal}</p>
                <p>Tuberculosis: ${data.Tuberculosis}</p>
                <p>Covid: ${data.Covid}</p>
                <p>Lung Opacity: ${data.Lung_Opacity}</p>
            `;
        } else {
            console.error('Error: ', data.error);
            // Implement user-friendly error message display
        }

    } catch (error) {
        console.error('Error', error);
        // Implement user-friendly error message display
    }
});
