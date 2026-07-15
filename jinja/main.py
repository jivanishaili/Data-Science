from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = "jack"
    languages = "python"
    luckynos = [1, 5, 54, 78, 99, 101]
    footer = "<p> Copyright 2025  | All rights reserved </P>"
    
    return render_template("index.html", name=name, lang=languages, lucky=luckynos, footer=footer)
 
app.run(debug = True)