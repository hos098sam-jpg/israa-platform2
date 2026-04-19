from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "منصة الإسراء شغالة 🔥"

if __name__ == "__main__":
    app.run()
