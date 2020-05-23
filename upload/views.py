from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import BookForm, CreateUserForm, UserUpdateForm,ProfileUpdateForm,TopicForm ,EntryForm,QueryForm
from .models import Book,Profile,Topic,Query,Entry
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

class Home(TemplateView):
    template_name= 'about_me.html'

def register_page(request):
    if request.user.is_authenticated:
        print("Logged in")
        return redirect('profile')

    else:
        print("Not logged in")
        forms = CreateUserForm()
        form = AuthenticationForm()
        if request.method =='POST' and 'btn2' in request.POST:
            forms = CreateUserForm(request.POST)
            if forms.is_valid():
                user = forms.save(commit=False)
                user.save()
                Profile.objects.create(user=user)

        if request.method =='POST' and 'btn1' in request.POST:
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request,user)
                if'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('profile')
        return render(request, 'register.html', {'forms':forms, 'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('register_page')

@login_required(login_url='register_page')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='register_page')
def profileupdate(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()
    context = { 'u_form':u_form, 'p_form':p_form}
    return render(request, 'profile_in.html',context)

def index(request):
    return render(request, 'about_me.html')

def delete_city(request, pk):
    Book.objects.get(pk= pk).delete()
    print(pk)
    return redirect('book_list')


@login_required(login_url='register_page')
def book_list(request):
    books = Book.objects.filter(owner=request.user)
    return render(request, 'book_list.html',{'books':books})

def book_all(request):
    books = Book.objects.filter()
    return render(request, 'all_book.html',{'books':books})

@login_required(login_url='register_page')
def upload_book(request):
    if request.method == 'POST':
        form = BookForm (request.POST, request.FILES,)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.owner = request.user; 
            obj.save() 
            return redirect('book_list')
    else:
        form = BookForm ()

    form = BookForm()
    return render(request, 'upload_book.html',{ 'form':form })


@login_required
def topic(request, pk):
    topic = Topic.objects.get(pk= pk)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries, }
    return render(request, 'topic.html', context)

@login_required(login_url='register_page')
def topics(request, pk):
    book = Book.objects.get(id=pk)
    topics = book.topic_set.order_by('-date_added')
    form = TopicForm (instance=book)
    if request.method == 'POST':
        form = TopicForm (request.POST, )
        if form.is_valid():
            obj = form.save(commit = False)
            obj.writer = request.user
            obj.owner = book 
            obj.save() 
            context = {'topics':topics ,'book':book,'form': form}
            return render(request, 'topics.html', context)
    context = {'topics':topics ,'book':book,'form': form}
    return render(request, 'topics.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user 
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic',args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'new_entry.html', context)

@login_required
def edit_entry(request,entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance = entry)
    else:
        form = EntryForm(instance= entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic',args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'edit_entry.html', context)

@login_required
def query(request):
    query = Query.objects.all()
    if request.method != 'POST':
        form = QueryForm()
    else:
        form = QueryForm(data=request.POST)
        if form.is_valid():
            new_q = form.save(commit=False)
            new_q.owner = request.user 
            new_q.save()
            return redirect('query')
    context = {'queries': query, 'topic': topic, 'form': form}
    return render(request, 'queris.html', context)
