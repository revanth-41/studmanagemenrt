from django.shortcuts import render,redirect
from .models import User,BlogPost,Access
from .forms import UserForm,BlogPostForm,UpdateProfilePicForm

from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User as Admin

def allUsersDetails(request):
    all_users = User.objects.all()
    context = {
        'users': all_users, 
        'accessors' : Access.objects.all().order_by('user_id')
    }
    # print(context['accessors'].objects.get(user_id=1).access)
    return render(request,"summaryPage.html",context)

def UserDetails(request,id):
    user = User.objects.get(id=id)
    # img = UserProfile.objects.filter(user=user).first()
    blogOfUser = BlogPost.objects.filter(author_id = user)
    context = {
        'user' : user,
        'blog' : BlogPostForm(),
        'blogs' : blogOfUser,
        # 'image' : img
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = BlogPost(title=title, content=content, author=user)
        post.save()
        
    return render(request,"UserPage.html",context)

def UpdateProfilePic(request,id):
    context = {
        'form': UpdateProfilePicForm(),
        # 'user' : user
    }
    user = User.objects.get(id=id)
    context['user']=user
    if request.method == 'POST':
        form = UpdateProfilePicForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('/app/home/details/{0}'.format(user.id))
    return render(request,'updatepic.html',context)


def adminUserDetails(request,id):
    user = User.objects.get(id=id)
    blogOfUser = BlogPost.objects.filter(author_id = user)
    context = {
        'blogs':blogOfUser, 
        'user' : user
    }
    return render(request,"AdminAccesUser.html",context)

def AccessEnableorDisable(request,id):
    # all_users = User.objects.all()
    # context = {
    #     'users': all_users, 
    #     'accessors' : Access.objects.all().order_by('user_id'),
    #     'user' : User.objects.get(id=id)
    # }
    user1 = User.objects.get(id=id)
    access_obj = Access.objects.get(user_id=user1)
    # print(access_obj)
    is_enabled=access_obj.access
    if is_enabled==True:
        access_obj.access = False
        access_obj.save()
    else:
        access_obj.access = True
        access_obj.save() 
    # user = context['user']    
    return redirect('/app/home/details/')     

def ShoworHideBlog(request,user_id,blog_id):
    user = User.objects.get(id=user_id)
    my_blog_id = BlogPost.objects.get(id=blog_id)
    is_enabled=my_blog_id.status
    if is_enabled==True:
        my_blog_id.status = False
        my_blog_id.save()
    else:
        my_blog_id.status = True
        my_blog_id.save() 
    return redirect('/app/home/details/{0}'.format(user.id))

def validate_mobile_number(value):
    """
    Validate that the input is a 10-digit mobile number.
    """
    value = str(value)
    if not value.isdigit() or len(value) != 10:
        # raise ValidationError("Please enter a 10-digit mobile number.")
        return False
    return True

def validate_password(password):
    """
    Validate the input password.
    """
    # Rule 1: Minimum length (e.g., at least 8 characters)
    if len(password) < 8:
        return False

    # Rule 2: Contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Rule 3: Contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Rule 4: Contains at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Rule 5: Contains at least one special character (e.g., !@#$%^&*)
    special_characters = "!@#$%^&*()_+[]{}|;:,.<>?/~`"
    if not any(char in special_characters for char in password):
        return False
    
    # All rules passed
    return True

# Create your views here.
def HomeView(request):
    """
    Display Home Page.
	It then renders a Homepage.html template to display
    the Buttons.

    Returns:
	It display the 3 Buttons
		-Admin SignIn
		-user SignIn
		-SignUp
		
    """
    return render(request,'HomePage.html')

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
                access_obj = Access.objects.get(user_id_id=user_obj.id)
                if access_obj.access == True:
                    return redirect('/app/home/details/{0}'.format(user_obj.id))
                else:
                    context['user'] = "Access Permission Denied"
                    return render(request,'UserLogin.html', context)
                # return render(request, "UserPage.html",context)
            else:
                context["user"] = "Incorrect password.."
                return render(request,'UserLogin.html', context)
        except:
            context["user"] = "User not found.."
            return render(request,'UserLogin.html', context)
    return render(request,'UserLogin.html',context)

def AdminLoginView(request):
    """
    Display Admin SignIn page.

    This view takes Admin-Email,password as a parameter and it will check from the database 
    based on that parameters,whether the admin is available or not
    It then renders a AdminLogin.html template to display the input fields-Email,password.
    If Admin is available then it renders a summaryPage.html template to display all the user details.
    Then it has a Logout button which renders to Homepage.

    Parameters:
        - Email
	- password

    Returns:
        - First it display the Admin login page with 2 input fields-Email,password.
	- Then it display Summery page which shows all details of users
    """
    context = {}
    context["users"] = ''
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        t = User.objects.all()
        try:
            a1 = Admin.objects.get(email=email)
            if check_password(password,a1.password):
                context['users'] = t
                return redirect('/app/home/details/')
                #return render(request, "summaryPage.html",context)
            else:
                context["users"] = "Incorrect password.."
                return render(request,'AdminLogin.html', context)
        except:
            context["users"] = "Admin not found.."
            return render(request,'AdminLogin.html', context)
    return render(request,'AdminLogin.html')

def Register(request):
    """
    Create a User via post request by displaying a Register page.

    This view handles POST requests to create a user. It expects all the required data fields. Upon successful creation of
    the object, it returns a message-User Registered successfully and it has phoneNumber validation and Password Validation.

    Request:
        - Method: POST

    Response:
        - User Registered successfully.
    
    If the request data is not valid, it an error message.

    Error Response:
        -phoneNumber validation-Please enter a 10 digit mobile number
	-Password Validation-Password should contain 8 characters and at least one special character,one uppercase letter,one lowercase letter and one digit
    """
    context = {}
    context['form'] = UserForm()
    context['data'] = ''
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
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            user = User.objects.get(email=request.POST.get("email"))
            context['user'] = user
            user_access_obj = Access(user_id=User.objects.get(email=request.POST.get("email")),access=True)
            user_access_obj.save()
            context['data']=f"{request.POST.get('name')} registered succefully"
            return render(request,'Register.html',context)
        else:
            print("Invalid Entry")
    return render(request,'Register.html',context)

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
        form = UserForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            context['data']=f"details updated successfully"
            return redirect('/app/home/details/{0}'.format(user.id))
            #return render(request,'Register.html',context)
        else:
            print("Invalid Entry")
    return render(request,'Register.html',context)

