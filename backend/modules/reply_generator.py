from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def generate_reply(email):

    prompt = f"Write a professional email reply to: {email}"

    response = generator(prompt, max_length=120)

    return response[0]["generated_text"]
