from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Server aktif 🌿"

@app.route("/<name>")
def love(name):
    return f"I Love You {name}"

if __name__ == "__main__":
    app.run()
