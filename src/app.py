from flask import Flask, render_template

app = Flask("__name__")

@app.route('/modulo1')
def modulo1():
    return render_template('modulo1.html')

