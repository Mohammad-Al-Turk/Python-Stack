from django.db import models
import bcrypt
import re

class UserManager(models.Manager):
    def mng(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    
            errors['email'] = "Invalid email address!"
            
        if len(postData['fname']) < 2:
            errors["fname"] = "First name should be at least 2 characters"
            
        if len(postData['lname']) < 2:
            errors["lname"] = "Last name should be at least 2 characters"
            
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
            
        if postData['password'] != postData['cpassword']:
            errors["password"] = "Password does not match"
        return errors
    
    
    
class PieManager(models.Manager):
    def mng(self, postData):
        errorsPie = {}
        if len(postData['name']) < 1:
            errorsPie["name"] = "Please include the name"

        if len(postData['filling']) < 1:
            errorsPie["filling"] = "Please include the filling"          

        if len(postData['crust']) < 1:
            errorsPie["crust"] = "Please include the crust"    

        return errorsPie
    

class User(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    email = models.CharField(max_length=45,unique=True)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()
    

class Pie(models.Model):
    name = models.CharField(max_length=45)
    filling = models.CharField(max_length=45)
    crust = models.CharField(max_length=45,unique=True)
    user = models.ForeignKey(User,related_name= "pies" , on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=PieManager()



def register_user(data):
    pw = data['password']
    pw_hash=bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()
    return User.objects.create(fname=data['fname'],lname=data['lname'],email=data['email'],password=pw_hash)

def save_pies(data):
    return Pie.objects.create(name=data['name'],filling=data['filling'],crust=data['crust'],user =User.objects.get(id=int(data["user"])))

def get_all():
    return User.objects.all()

def get_all_User():
    return User.objects.all()

def get_all_pie():
    return Pie.objects.all()


def deleteId(id):
    c=Pie.objects.get(id=id)
    c.delete()
    
    
def editId(data):
    id=data['edit_id']
    c=Pie.objects.get(id=id)
    c.name=data['name']
    c.filling=data['filling']
    c.crust=data['crust']
    c.save()
    
    
def showData_by_id(id):
    return Pie.objects.get(id=id)


