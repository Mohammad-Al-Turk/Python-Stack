from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    nameFromIndex=request.form['name']
    locationFromIndex=request.form['location']
    languageFromIndex=request.form['language']
    CommentsFromIndex=request.form['Comments']
    return render_template('show.html' ,name= nameFromIndex,location=locationFromIndex,language=languageFromIndex,Comments=CommentsFromIndex)
    
#الصح انه نستخدم ري دايركت مع البوست ثم رندر


if __name__=="__main__":
    app.run(debug=True)