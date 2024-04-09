from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import cv2
from keras.preprocessing import image
import os
import pandas as pd

# Load the model outside the function for efficiency
classifierLoad = tf.keras.models.load_model('model.h5')

app = Flask(__name__)

# Configure uploads folder (replace with your desired path)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Dictionary to store information for each food category
food_info = {
    "briyani": "High in calories, saturated fats, and may lack balanced nutrition.",
    "burger": "Loaded with unhealthy fats, calories, and sodium, contributing to poor cardiovascular health.",
    "dosa": "High glycemic index and potential for unhealthy frying methods.",
    "idly": "Low in essential nutrients and may lead to blood sugar spikes.",
    "soup": "Some varieties may be high in sodium and lack sufficient nutrients.",
    "pizza": "Often high in calories, saturated fats, and sodium.",
    "noodles": "Often processed and high in sodium, leading to potential health issues."
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def upload_form():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

@app.route('/service')
def service():
    return render_template('home.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/upload", methods=["POST"])
def handle_upload():
    # Get the uploaded image file
    image_file = request.files["image"]
    
    # Check if an image is uploaded
    if image_file:
        try:
            # Save the image in uploads folder
            filename = image_file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(filepath)
            print(f"Image saved: {filepath}")  # Print path for verification

            # Process the image (assuming the saved file)
            test_image = image.load_img(filepath, target_size=(200, 200))
            test_image_color = cv2.imread(filepath)  # Load image in color

            # Preprocess the image (assuming test_image is loaded)
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
        
            # Classify the image
            result = classifierLoad.predict(test_image)
            
            # Interpret results based on prediction
            predicted_class = np.argmax(result[0])
            class_names = ["briyani", "burger", "dosa", "idly", "noodles", "pizza", "soup"]
            
            if predicted_class not in range(len(class_names)):
                # Redirect to not_valid.html
                return render_template("not_valid.html")
            
            predicted_food = class_names[predicted_class]
            
            # Get additional information based on predicted category
            food_info_text = food_info.get(predicted_food, "No additional information available for this food category.")
            
            # Calculate calories based on predicted food category
            calories = calculate_calories(predicted_food)  # Pass predicted_food to the function
            
            # Save the color-converted image temporarily
            cv2.imwrite('color_image.jpg', test_image_color)
            
            # Pass the paths and information to the result template
            return render_template("result.html", predicted_food=predicted_food, food_info=food_info_text, 
                                   color_image='color_image.jpg', calories=calories)
        except Exception as e:
            return f"Error processing image: {str(e)}"
    else:
        return "No image uploaded!"


# Define calculate_calories() function outside the handle_upload() function
def calculate_calories(predicted_food):
    # Define a dictionary mapping food categories to calorie values
    calorie_values = {
        "briyani": 500,   # Adjust these values according to your data
        "burger": 600,
        "dosa": 300,
        "idly": 150,
        "noodles": 400,
        "pizza": 700,
        "soup": 200
    }
    
    # Get the calorie value for the predicted food category
    calories = calorie_values.get(predicted_food, "Calorie information not available")
    return calories




if __name__ == "__main__":
    app.run(debug=True)
