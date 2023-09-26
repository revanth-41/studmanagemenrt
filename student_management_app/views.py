from django.shortcuts import render,redirect
from .models import User


def validate_mobile_number(value):
    """
    Validate that the input is a 10-digit mobile number.
    """
    value = str(value)
    if not value.isdigit() or len(value) != 10:
        # raise ValidationError("Please enter a 10-digit mobile number.")
        return False
    return True

# Create your views here.
def UserLoginView(request):
    """
    Display user SignIn page.

    This view takes User-Email,password as a parameter and it will check from the database 
    based on that parameters,whether the user is available or not
    It then renders a UserLogin.html template to display the input fields-Email,password.
    If User is available then it renders a UserPage.html template to display their details.
    Then it has a Logout button which renders to Homepage.

    Parameters:
        - Email
	- Password

    Returns:
        - First it display the User login page with 2 input fields-Email,password.
	- Then it display User page which shows the details of user
    """
    context = {}
    context["user"] = ''
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user_obj = User.objects.get(email=email)
            if password == user_obj.password:
                context['user'] = user_obj
                return redirect('/app/home/details/{0}'.format(user_obj.id))
                # return render(request, "UserPage.html",context)
            else:
                context["user"] = "Incorrect password.."
                return render(request,'UserLogin.html', context)
        except:
            context["user"] = "User not found.."
            return render(request,'UserLogin.html', context)
    return render(request,'UserLogin.html',context)
