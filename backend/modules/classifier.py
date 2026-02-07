import joblib
import os
from .preprocessor import clean_text

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def classify_spam(email_text):

    cleaned = clean_text(email_text)

    transformed = vectorizer.transform([cleaned])

    prediction = model.predict(transformed)[0]

    # Convert numpy value to Python int
    pred_int = int(prediction)

    if pred_int == 1:
        return "spam"
    else:
        return "not_spam"


