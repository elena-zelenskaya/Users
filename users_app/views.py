from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    context = {
        "users": User.objects.all()
	}
    return render(request, "index.html", context)

def add_user(request):
    if request.method == "POST":
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        email_address = request.POST["email"]
        age = request.POST["age"]
        User.objects.create(first_name = first_name, last_name = last_name, email_address = email_address, age = age)
    return redirect("/")

def delete_user(request, id):
    User.objects.get(id=id).delete()
    return redirect("/")

def edit_user(request, id):
    context = {
        "user_to_edit": User.objects.get(id=id)
	}
    return render(request, "edit.html", context)

def update_user(request, id):
    user_to_update = User.objects.get(id=id)
    if request.method == "POST":
        if request.POST["fname"]:
            user_to_update.first_name = request.POST["fname"]
        if request.POST["lname"]:
            user_to_update.last_name = request.POST["lname"]
        if request.POST["email"]:
            user_to_update.email_address = request.POST["email"]
        if request.POST["age"]:
            user_to_update.age = request.POST["age"]
        user_to_update.save()
    return redirect("/")
