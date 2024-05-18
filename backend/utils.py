"""
Utility functions for the web app
"""

import os

from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
from config import loaded_model
from flask import jsonify
# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"


classification_classes = {
    0: 'Normal',
    1: 'Tuberculosis',
    2: 'Covid',
    3: 'Lung_Opacity'
}

def preprocess_image(image) -> np.array:
    """
    Here the input image is preprocessed for classification

    Parameters: 
    image (PIL.image): This is the input image to be preprocessed

    It returns the preprocessed images as a Numpy array - np.array
    """
    image = Image.open(image).convert("RGB").resize((224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image

def classify_image(image: np.array) -> str:
    
    classification = loaded_model.classify(image, verbose=0)[0]
    classified_label = classification_classes[np.argmax(classification)]
    return {
        "classification": classified_label,
        "Normal": round(float(classification[0]), 6),
        "Tuberculosis": round(float(classification[1]), 6),
        "Covid": round(float(classification[2]), 6),
        "Lung_Opacity": round(float(classification[3]), 6)
    }

