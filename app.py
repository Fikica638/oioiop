from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    print(f"Message received from {name} ({email}): {message}")
    return "Thank you for your message!"

if __name__ == "__main__":
    app.run(debug=True)
