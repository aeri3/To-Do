from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import Http404
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from .models import Entry, Checklist


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username, password)
        login(request,user)
        return redirect("todo:home")

    return render(request, 'todo/accounts.html', {})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('todo:home')
        else:
            return HttpResponse("Invalid Account : Sign Up.")

    else:      
        return render(request, 'todo/accounts.html', {})
    

@login_required(login_url='/todo/signin')


def logout_view(request):
    logout(request)
    return redirect("todo/accounts.html")

def accounts(request):
    return render(request, 'todo/accounts.html')


def home(request):
    todos = Entry.objects.order_by('-pub_date')[:5]

    
    context = {'todos' : todos}

    return render(request, 'todo/home.html', context)

def post(request):
    text = request.POST['entry']
    title = request.POST['title']
    entry_user = Entry(text=text, title=title, author=request.user)
    
    entry_user.save()

    return redirect('todo:home')

def entries(request):
    current_date = datetime.now()
    return render(request, 'todo/entries.html', {'current_date': current_date})

def list(request):
    current_date = datetime.now()
    return render(request, 'todo/list.html',  {'current_date': current_date})

def delete(request, entry_id):
     dell = Entry.objects.get(id=entry_id)  
     dell.delete()
     return redirect(request.META['HTTP_REFERER'])   

def entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    context = {'entry' : entry}
    return render(request, 'todo/entry.html', context)


def checklist(request):
    checklist_items = Checklist.objects.all()
    current_date = datetime.now()
    context = {'checklist_items': checklist_items, 'current_date': current_date}
    return render(request, 'todo/checklist.html', context)

def add_checklist(request):
    value = request.POST['new_item']
    cl = Checklist(title=value, author=request.user)
    cl.save()

    return redirect(request.META['HTTP_REFERER'])

def delete_checklist(request, checklist_id):
    return redirect(request.META['HTTP_REFERER'])

def add_item(request):
    if request.method == 'POST':
        print(request.POST)
        new_item = request.POST['new_item']
        Checklist.objects.create(item=new_item)
    return redirect('todo:checklist')

def toggle_item(request, item_id):
    item = Checklist.objects.get(pk=item_id)
    item.completed = not item.completed
    item.save()
    return redirect('todo:checklist')

def delete_item(request, item_id):
    item = Checklist.objects.get(pk=item_id)
    item.delete()
    return redirect('todo:checklist')