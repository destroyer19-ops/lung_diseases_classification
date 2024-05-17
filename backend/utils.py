"""
Utility functions for the web app
"""

import os
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
from config import loaded_model
from flask import jsonify


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

