document.getElementById(uploadForm).addEventListener('submit', async function (e) {
    e.preventDefault();
    const formData = new FormData();
    const fileField = document.getElementById('inputImage').files[0];

    formData.append('file', fileField);

    try {


        const response = await fetch('/classsify', {
            method: 'POST',
            body: 'formData'
        })
        const data = await response.json()

        if (response.ok) {
            document.getElementById('results').style.display = 'block'
            document.getElementById('imgName').textContent = fileField.name;
            document.getElementById('normalValue').textContent = data.Normal;
            document.getElementById('tuberculosisValue').textContent = data.Tuberculosis;
            document.getElementById('covidValue').textContent = data.Covid;
            document.getElementById('lungOpacityValue').textContent = data.Lung_Opacity;
            document.getElementById('diagnosisValue').textContent = data.classification;
        } else {
            console.log('Error ' + data.error);
        }

    } catch (error) {
        console.error('Error', error);
    }
})
