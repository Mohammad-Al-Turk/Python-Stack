from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  



@app.route('/')         
def index():
    return render_template("index.html")





@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    select1=request.form['strawberry']
    select2=request.form['raspberry']
    select3=request.form['apple']
    name1=request.form['first_name']
    name2=request.form['last_name']
    id=request.form['student_id']
    total=int(select1)+int(select2)+int(select3)
    time=datetime.now().strftime("%D / %m / %Y | %H:%M: %S")
    
    
    return render_template("checkout.html",selecter1=select1,selecter2=select2,selecter3=select3,fname=name1,lname=name2,id_num=id,items=total,time=time)

#الصح استخدام ري دايركت مع البوست ثم رندر



@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")





if __name__=="__main__":   
    app.run(debug=True)    