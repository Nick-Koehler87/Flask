from flask import Flask, render_template, request

app = Flask(__name__)

peps = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template("register.html", peps=peps)

@app.route('/submit', methods=['Post'])
def submit():
    name = request.form.get('name')
    org = request.form.get('org')
    dude = Person(name, org)
    peps.append(dude)
    return render_template("index.html")

class Person():
    def __init__(self, name, org):
        self.name = name
        self.org = org

    def print(self):
        return str('NAME = ' + self.name + '    ORG = ' + self.org)

    

