from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/')
def home():
    return 'Hello, Data Scientist!'


@app.route('/about')
def about():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return '<P>Hello, I am contact page!<p>'

app.run(debug=True)