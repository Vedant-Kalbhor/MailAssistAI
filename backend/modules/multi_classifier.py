# from transformers import pipeline

# classifier = pipeline(
#     "text-classification",
#     model="distilbert-base-uncased-finetuned-sst-2-english"
# )

# def classify_multi(email):

#     result = classifier(email)[0]

#     label = result["label"]

#     if "NEGATIVE" in label:
#         return "spam"

#     return "important"
from transformers import pipeline
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "transformer_classifier")

classifier = pipeline(
    "text-classification",
    model=MODEL_PATH,
    tokenizer=MODEL_PATH
)

label_map = {
    "LABEL_0": "spam",
    "LABEL_1": "important",
    "LABEL_2": "follow_up",
    "LABEL_3": "normal"
}

def classify_multi(email):

    result = classifier(email)[0]

    label = result["label"]

    return label_map[label]
