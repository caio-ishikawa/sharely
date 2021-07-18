from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import File, Folder
from .forms import FileForm, FolderForm

def homepage(request):
    if request.user.is_authenticated:
        files = File.objects.filter(user=request.user)
        folders = Folder.objects.filter(user=request.user)
        return render(request, 'main/homepage.html', {'files':files, 'folders':folders})
    else:
        return  render(request, 'main/homepage.html')


def registerView(request):
    form = UserCreationForm(request.POST)

    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        login(request, user)
        return redirect('/')

    return render(request, 'main/register.html', {'form':form})


def loginView(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
    return render(request, 'main/login.html',  {'form':form})


def logoutView(request):
    logout(request)
    return redirect('/')

def uploadView(request):
    form = FileForm(request.POST, request.FILES)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('/')

    else:
        print(form.errors)

    return render(request, 'main/upload.html', {'form': form})


def folderView(request, pk):
    folders =  Folder.objects.filter(pk=pk)
    return render(request, 'main/folder.html', {'folders':folders})


def createFolder(request):
    form = FolderForm(request.POST)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('/')

    return render(request, 'main/add_folder.html', {'form':form})

def addFile(request, pk, id):
    folder = Folder.objects.get(pk=id)
    new_file = File.objects.get(pk=pk)
    folder.file.add(new_file)
    return redirect('/')
