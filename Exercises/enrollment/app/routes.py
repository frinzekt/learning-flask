from app import app

@app.route("/")
@app.route("/index")
def index():
    return"<h1>Hello Eart1h!</h1>"