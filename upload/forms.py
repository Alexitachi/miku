from django import forms  
from .models import Book,Profile,Topic,Entry,Query
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','pdf','cover']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields ={'username','email','password1','password2'}

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email',]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','description','li','insta',]

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text',]
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}