from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def classify_multi(email):

    result = classifier(email)[0]

    label = result["label"]

    if "NEGATIVE" in label:
        return "spam"

    return "important"
