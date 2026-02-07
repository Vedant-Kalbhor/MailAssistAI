from flask import Flask
from flask_cors import CORS
from routes.classify_routes import classify_bp,multi_bp
from routes.email_routes import email_bp
from routes.reply_routes import reply_bp

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "AI Email Assistant Running"


app.register_blueprint(multi_bp)

app.register_blueprint(email_bp)

app.register_blueprint(classify_bp)

app.register_blueprint(reply_bp)


if __name__ == "__main__":
    app.run(debug=True)
