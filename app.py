from flask import Flask

app = Flask(__name__)

@app.route("/")
def show_landing_page() -> str:
    print("Inside shop")
    print("Will write more logic later on.")
    return "Hello from Ashwini on the landing page v.0.0.2!"

@app.route("/usa")
def home() -> str:
    print("Inside ghar.")
    print("Will write more logic later on.")
    return "Hello from Ashwini inside home Function v.0.0.1!"

@app.route("/usa-store")
def shop() -> str:
    print("Inside shop")
    print("Will write more logic later on.")
    return "Hello from Ashwini inside shop Function v.0.0.1!"