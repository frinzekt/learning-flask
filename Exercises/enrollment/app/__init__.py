from flask import Flask

app = Flask(__name__) #Name of Current instance offlask

@app.route("/")
@app.route("/index")
def index():
    return"<h1>Hello Eart1h!</h1>"