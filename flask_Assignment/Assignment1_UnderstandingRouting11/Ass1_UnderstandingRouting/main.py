from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"



@app.route('/')          
def hello_world():
    return 'Hello World!'  


@app.route('/Champion')
def Champion():
    return "Champion"


@app.route('/say/Flask')
def sayFlask():
    return "Hi, Flask"


@app.route('/say/Michael')
def sayMichael():
    return "Hi, Michael"


@app.route('/say/john')
def sayJohn():
    return "Hi, John"


@app.route('/repeat/<text>/<times>')
def repeat(text,times):
    return "have it say " + text +" "+ times +" times"



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.