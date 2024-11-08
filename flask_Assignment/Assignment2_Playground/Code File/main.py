from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def Playground():
    return render_template("index.html", times=3)


@app.route('/play/<int:x>')
def Playground_Manual(x):
    return render_template("index.html", times=x)



@app.route('/play/<int:x>/<color>')
def Playground_Manual_with_color(x,color):
    return render_template("index.html", times=x, colors=color)

if __name__=="__main__":
    app.run(debug=True)