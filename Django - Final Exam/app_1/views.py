from django.shortcuts import *
from django.contrib import messages
# from .models import Show
# from .models import ShowManager
from . import models
from .models import *


def main(request):
    return render(request,'main.html')


def dash(request):
    user = User.objects.get(id=request.session['id'])
    context={
        'user': user
    }
    return render(request,'dash.html',context)

def register(request):
    
    if request.method == 'POST':
        errors = User.objects.mng(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            register_user(request.POST)
            if 'fname' not in request.session:
                em = request.POST.get('email')
                user = User.objects.get(email=em)
                request.session['fname']=user.fname
                request.session['id']=user.id
            return redirect('/dash')
    else:
        return HttpResponse('error 404')


def dashboard_login(request):
    if request.method == 'POST':
        em = request.POST.get('email')
        pw = request.POST.get('password')
        if User.objects.filter(email=em).exists():
            user = User.objects.get(email=em)
            request.session['fname']=user.fname
            request.session['id']=user.id
            
            try:
                if bcrypt.checkpw(pw.encode(), user.password.encode()):
                    messages.success(request, "Login successful!")
                    return redirect('/dash')
                else:
                    messages.error(request, "Invalid password. Please try again.")
                    return redirect('/')
            except User.DoesNotExist:
                messages.error(request, "User does not exist.")
                return redirect('/')

        else:
            messages.error(request, "This email is not registered. You must register first.")
            return redirect('/')
    else:
        return HttpResponse("Error")
    




def save_pie(request):
    
    if request.method == 'POST':
        errorsPie = Pie.objects.mng(request.POST)
        if len(errorsPie) > 0:
            for key, value in errorsPie.items():
                messages.error(request, value)
            return redirect('/dash')
        else:
            save_pies(request.POST)
            return redirect('/dash')
    else:
        return HttpResponse('error 404')
    
    

    
    

def delete_by_id(request,id):
    deleteId(id)
    return redirect('/dash')




def clearSession(request):
    request.session.clear()
    return redirect('/')



def edit_by_id(request,id):
    context={
       'show': showData_by_id(id)
    }
    return render(request,'edit.html',context)


def update(request):
    if request.method == 'POST':
        errorsPie = Pie.objects.mng(request.POST)
        if len(errorsPie) > 0:
            for key, value in errorsPie.items():
                messages.error(request, value)
            return redirect('/update')
        else:
            editId(request.POST)
            return redirect('/dash')
        
    else:
        return HttpResponse("Error 404") 
    
    
    
    
def show_all(request):
    context={
        
        'all_user': get_all_User(),
        'all_Pir':get_all_pie()
        
    }
    return render(request,'allPie.html',context)
    
    
    
def details(request):
    em = request.POST.get('email')
    pw = request.POST.get('password')
    if User.objects.filter(email=em).exists():
        user = User.objects.get(email=em)
        request.session['fname']=user.fname
        request.session['id']=user.id
    return render(request,'details.html')



