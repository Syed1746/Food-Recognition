from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from keras.preprocessing import image
import os

# Load the model outside the function for efficiency
classifierLoad = tf.keras.models.load_model('model.h5')

app = Flask(__name__)

# Configure uploads folder (replace with your desired path)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define food categories
food_categories = ["briyani", "burger", "dosa", "idly", "noodles", "pizza", "soup"]

@app.route("/api/add-image", methods=["POST"])
def add_image():
    # Get the uploaded image file
    image_file = request.files["image"]
    
    # Check if an image is uploaded
    if image_file:
        try:
            # Save the image in uploads folder
            filename = image_file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(filepath)

            # Process the image (assuming the saved file)
            test_image = image.load_img(filepath, target_size=(200, 200))

            # Preprocess the image (assuming test_image is loaded)
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
        
            # Classify the image
            result = classifierLoad.predict(test_image)
            
            # Interpret results based on prediction
            predicted_class = np.argmax(result[0])
            predicted_food = food_categories[predicted_class]
            
            # Prepare JSON response
            response_data = {
                "img_url": "api.foodron.ai/img-url",  # Replace with actual URLs
                "inf_img_url": "api.foodron.ai/inf-img-url",
                "item_count": 1,
                "item_class": [predicted_food],
                "items": [{
                    "name": predicted_food,
                    "serve": 1,
                    "weight": 100,  # Placeholder values, replace with actual data
                    "calorie": 200,
                    "carbohydrates": 30,
                    "fiber": 5,
                    "fat": 15,
                    "protein": 20,
                    "sugar": 10
                }]
            }
            
            return jsonify(response_data)
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "No image uploaded!"}), 400

if __name__ == "__main__":
    app.run(debug=True)
