# from flask import Flask  # Import Flask to allow us to create our app
# app = Flask(__name__)    # Create a new instance of the Flask class called "app"



# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response



# @app.route('/login')          # The "@" decorator associates this route with the function immediately following
# def login():
#     return 'login'  # Return the string 'Hello World!' as a response




# @app.route('/success')
# def success():
#     return "success"




# @app.route('/hello/<name>')
# def hello(name):
#     return "Hello, " + name



# @app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id



# if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
#     app.run(debug=True)    # Run the app in debug mode.





# # /hello_flask/hello.py
# from flask import Flask, render_template  # إضافة render_template

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     # بدلاً من إعادة نص، نستخدم render_template لعرض ملف HTML
#     return render_template('hello.html')

# if __name__=="__main__":
#     app.run(debug=True)





# hello_flask/hello.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # تمرير البيانات مع الملف HTML
    return render_template("hello.html", phrase="hello", times=5)

if __name__=="__main__":
    app.run(debug=True)