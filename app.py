from flask import Flask, render_template, request, jsonify
from PIL import Image
import pytesseract
import os

app = Flask(__name__)

# Path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# List of harmful ingredients to check for
harmful_ingredients = [
    'Phthalates', 'Paraben', 'Sulfate', 'Fragrance', 'Triclosan', 'Synthetic colors', 'Toluene', 'Lead', 'Formaldehyde'
    # Add more ingredients as needed
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    # Save the uploaded file
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    # Process the image and check for harmful ingredients
    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        harmful_found = [ingredient for ingredient in harmful_ingredients if ingredient.lower() in text.lower()]
        return jsonify({'text': text, 'harmful_found': harmful_found})
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)
