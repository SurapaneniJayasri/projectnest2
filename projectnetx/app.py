from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/prediction')
def prediction():
    return render_template('prediction.html')
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')
@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

if __name__ == '__main__':
    app.run(debug=True)