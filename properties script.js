document.getElementById('houseForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const title = document.getElementById('title').value;
    const price = document.getElementById('price').value;
    const bedrooms = document.getElementById('bedrooms').value;
    const bathrooms = document.getElementById('bathrooms').value;
    const sqft = document.getElementById('sqft').value;
    const imageFile = document.getElementById('image').files[0];

    // Create a FileReader to read the uploaded image
    const reader = new FileReader();
    reader.onload = function(e) {
        const propertiesDiv = document.getElementById('properties');

        // Create a new property div
        const propertyDiv = document.createElement('div');
        propertyDiv.classList.add('property');

        // Add the image and details to the property div
        propertyDiv.innerHTML = `
            <img src="${e.target.result}" alt="${title}" style="max-width: 200px; height: auto;">
            <h3>${title}</h3>
            <p>Price: R${price}</p>
            <p>Bedrooms: ${bedrooms}</p>
            <p>Bathrooms: ${bathrooms}</p>
            <p>Square Footage: ${sqft} sqft</p>
        `;

        // Append the new property div to the properties section
        propertiesDiv.appendChild(propertyDiv);
    };

    // Read the image file as a data URL
    if (imageFile) {
        reader.readAsDataURL(imageFile);
    }

    // Reset the form
    document.getElementById('houseForm').reset();
});