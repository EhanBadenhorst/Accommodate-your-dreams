from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Flats.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from form
    title = request.form['title']
    price = request.form['price']
    bedrooms = request.form['bedrooms']
    bathrooms = request.form['bathrooms']
    sqft = request.form['sqft']
    contact_info = request.form['contactInfo']
    location = request.form['location']
    image_file = request.files['image']

    # Save the text data to Avalinel flats.txt
    with open('Avalinel flats.txt', 'a') as file:
        file.write(f"Title: {title}\n")
        file.write(f"Price: R{price}\n")
        file.write(f"Bedrooms: {bedrooms}\n")
        file.write(f"Bathrooms: {bathrooms}\n")
        file.write(f"Square Footage: {sqft} sq ft\n")
        file.write(f"Contact Information: {contact_info}\n")
        file.write(f"Location: {location}\n")
        file.write("---\n")  # Separator between entries

    # Save the uploaded image
    if image_file:
        image_path = os.path.join('static/images', image_file.filename)
        image_file.save(image_path)

    return redirect(url_for('view_properties'))

@app.route('/view-properties')
def view_properties():
    # Read data from Avalinel flats.txt
    with open('Avalinel flats.txt', 'r') as file:
        content = file.read()
    
    # Parse the content into a list of dictionaries
    properties = []
    entries = content.split('---')
    for entry in entries:
        if entry.strip():
            property_dict = {}
            lines = entry.strip().split('\n')
            for line in lines:
                key, value = line.split(': ', 1)
                property_dict[key] = value
            properties.append(property_dict)

    return render_template('View property for flats.html', properties=properties)

if __name__ == '__main__':
    app.run(debug=True)