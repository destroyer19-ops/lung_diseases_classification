"""
Create Flask App, load model and define CORS
"""
import os
from flask import Flask
from flask_cors import CORS
# import os
from tensorflow.keras.models import load_model
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

app = Flask(__name__)
CORS(app)
x = "./model/malaria_diagnosis_mobilenetv3Small.keras"
loaded_model = load_model(x)