from flask import Flask

app = Flask(__name__)

@app.route("/feed/")
def page_feed():
    return "Лента пользователя"

app.run()
