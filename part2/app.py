from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/calculate')
def calculate():
    return render_template('calculate.html', number=x)


@app.route('/submit')
def submit(): 
    try:
        fnum = int(request.args.get('fnum'))
    except:
        return render_template('calculateError.html')
    x = fnum % 2
    if x == 1:
        return render_template('calculateOdd.html', num=fnum)
    else:
        return render_template('calculateEven.html', num=fnum)