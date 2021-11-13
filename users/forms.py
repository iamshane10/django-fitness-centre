from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Employee, Review

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']

class ProfileForm(forms.ModelForm):   
    phone       = forms.CharField()
    address     = forms.CharField()
    gender      = forms.ChoiceField(choices = (("Male","Male"),("Female","Female")))
    height      = forms.DecimalField()
    weight      = forms.DecimalField()
    goals       = forms.ChoiceField(choices = (('Weight Loss','Weight Loss'),('Increase Muscle Mass','Increase Muscle Mass'),('Maintain Fitness','Maintain Fitness')))
    time        = forms.ChoiceField(choices = (("10am","10am"), ("11am","11am"), ("12pm","12pm"),("1pm","1pm"),("2pm","2pm"),("3pm","3pm"),("4pm","4pm"),("5pm","5pm"),("6pm","6pm"),("7pm","7pm"),("8pm","8pm")))
    
    class Meta:
        model = Profile
        fields = ['phone','address','gender','height','weight','goals','time']

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class EmployeeForm(forms.ModelForm):
    phone       = forms.CharField()
    gender      = forms.ChoiceField(choices = (("Male","Male"),("Female","Female")))

    class Meta:
        model = Employee
        fields = ['phone','gender']

class ReviewForm(forms.ModelForm):
    name         = forms.CharField()
    email        = forms.EmailField()
    thoughts     = forms.CharField()

    class Meta:
        model = Review
        fields = ['name','email','thoughts']