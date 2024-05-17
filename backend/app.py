import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
from flask import request, jsonify
from config import app
from utils import classify_image, preprocess_image

@app.route("/classify", methods=["POST"])
def classify():
    # 'classify' is the route of the api used to submit input images
    if "smear_image" not in request.files:
        return "Error"
    else:
        smear_image = request.files.getlist("smear_image")[0]
        img_array = preprocess_image(smear_image)
        classification = classify_image(img_array)
        return jsonify(classification)
    


if __name__ == "__main__":
    app.run(debug=False)