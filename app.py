from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
from pathlib import Path

app = Flask(__name__)
MODEL_PATH = Path("models/house_price_model.pkl")

def load_model():
    if not MODEL_PATH.exists():
        return None
    return joblib.load(MODEL_PATH)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    model = load_model()
    if model is None:
        return jsonify({"error": "Model abhi train nahi hua. Pehle terminal mein: python train_model.py run karo."}), 400

    try:
        values = [
            float(request.form["income"]),
            float(request.form["age"]),
            float(request.form["rooms"]),
            float(request.form["bedrooms"]),
            float(request.form["population"]),
        ]
        if any(v < 0 for v in values):
            return jsonify({"error": "Please zero ya positive values enter karo."}), 400

        prediction = float(model.predict(np.array([values]))[0])
        return jsonify({"price": round(prediction, 2)})
    except (ValueError, KeyError):
        return jsonify({"error": "Saare fields mein valid numbers enter karo."}), 400

if __name__ == "__main__":
    app.run(debug=True)
