from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os


app = Flask(__name__)
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = os.environ['EMAIL']
app.config["MAIL_PASSWORD"] = os.environ['PASSWORD']
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
mail = Mail(app)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("fname")
        email = request.form.get("uemail")
        msg = Message(f"From {name} {email}",
                      sender="meme@demo.com", recipients=["megadrugsazura@yahoo.com"])
        msg.body = "Whats up?"
        mail.send(msg)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
