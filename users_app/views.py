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
