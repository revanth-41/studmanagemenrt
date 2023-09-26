from django.shortcuts import render
from .models import User
from .forms import UserForm

# Create your views here.

def update(request,id):
    """
    Update a user via POST request by displaying a Register page with their existing user details.

    This view handles POST requests to update an existing user identified
    by id. It expects form data with the fields to be updated. Upon
    successful update of the object, it returns a message-details updated successfully.
    Then it has a Logout button which renders to Homepage.

    Request:
        - Method: POST
        - URL Parameters:
            - User Id(int)

    Response:
        - details updated successfully
    """    
    context = {}
    user = User.objects.get(id=id)
    context['form'] = UserForm(request.POST or None, instance=user)
    context['data'] = ''
    context['btval'] = 'Update'
    if request.method == 'POST':
        if not  validate_mobile_number(request.POST.get("phoneNumber")) and not validate_password(request.POST.get("password")):
            context['data'] = "Please enter a 10-digit mobile number and Password should contain 8 characters and at least one special character,one uppercase letter,one lowercase letter and one digit."
            return render(request,'Register.html',context)
        elif not validate_password(request.POST.get("password")):
            context['data'] = "Password should contain 8 characters and at least one special character,one uppercase letter,one lowercase letter and one digit."
            return render(request,'Register.html',context)
        elif not  validate_mobile_number(request.POST.get("phoneNumber")):
            context['data'] = "Please enter a 10 digit mobile number"
            return render(request,'Register.html',context)
        form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            context['data']=f"details updated successfully"
            return render(request,'Register.html',context)
        else:
            print("Invalid Entry")
    return render(request,'Register.html',context)
