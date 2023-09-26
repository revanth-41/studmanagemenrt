from django.shortcuts import render
from .models import User
# Create your views here.

def UserDetails(request,id):
    user = User.objects.get(id=id)
    context = {
        'user' : user
    }
    return render(request,"UserPage.html",context)

