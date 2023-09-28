from django import forms
from .models import User,BlogPost
# from matplotlib import widgets

from django.core.exceptions import ValidationError

from django.forms import TextInput,EmailInput,NumberInput,Select,Textarea


class UserForm(forms.ModelForm):
    # phoneNumber = forms.IntegerField(validators=[validate_mobile_number])
    # password = forms.CharField()

    gender = forms.ChoiceField(widget=forms.RadioSelect,
                           choices=(     
                                ("M", "Male"),
                                ("F", "Female"),
                                ("O","Other")))
    Qualification = forms.ChoiceField(choices=(
    ("SSC","SSC"),
    ("Inter","Inter"),
    ("Degree","Degree"),
    ("PG","PG")
    ))
    class Meta:
        model=User
        fields="__all__"
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 280px;height: 18px;padding: 7px;border-radius: 10px;border-width: 1px;border-color: rgba(0, 0, 0, 0.2);',
                'placeholder': 'Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'width: 280px;height: 18px;padding: 7px;border-radius: 10px;border-width: 1px;border-color: rgba(0, 0, 0, 0.2);',
                'placeholder': 'Email'
                }),
            'phoneNumber' : NumberInput(attrs={
                'class': "form-control", 
                'style': 'width: 280px;height: 18px;padding: 7px;border-radius: 10px;border-width: 1px;border-color: rgba(0, 0, 0, 0.2);',
                'placeholder': 'Phone Number'
                }),
            'Qualification' : Select(attrs={
                'class': "form-control", 
                'style': 'width: 280px;height: 18px;padding: 7px;border-radius: 10px;border-width: 1px;border-color: rgba(0, 0, 0, 0.2);',
                }),
            'Address' : Textarea(attrs={
                'rows' : 4,
                'cols' : 50,
                'style': 'width: 280px;padding: 7px;border-radius: 10px;border-width: 1px;border-color: rgba(0, 0, 0, 0.2);',
                'placeholder': 'Address'
                }),    
            'username' : TextInput(attrs={
                'class': "form-control", 
                'style': 'width: 280px;height: 18px;padding: 7px;border-radius: 10px;border-width: 1px;border-color: rgba(0, 0, 0, 0.2);',
                'placeholder': 'User Name'
                }), 
            'password': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 280px;height: 18px;padding: 7px;border-radius: 10px;border-width: 1px;border-color: rgba(0, 0, 0, 0.2);',
                'placeholder': 'Password'
                }),
                }

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','content']
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 400px;height: 18px;padding: 7px;border-radius: 10px;border-width: 1px;border-color: rgba(0, 0, 0, 0.2);font-family: Georgia;font-weight:bold;',
                'placeholder': 'Title'
                }),
            'content':  Textarea(attrs={
                'rows' : 10,
                'cols' : 50,
                'style': 'width: 400px;padding: 7px;border-radius: 10px;border-width: 1px;border-color: rgba(0, 0, 0, 0.2);font-family: Georgia;font-weight:bold;',
                'placeholder': 'Enter Blog'
                }), 
            } 

class UpdateProfilePicForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image']        