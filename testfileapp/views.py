from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from testfileapp.models import UploadFile
from testfileapp.forms import UserForm, UploadFileForm
import datetime

# Create your views here.


def red(request):
    return redirect(home)


def home(request):
    files = UploadFile.objects.all()

    if request.method == 'POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)

        if upload_file_form.is_valid():
            form = upload_file_form.save(commit=False)
            form.author = request.user
            form.date = datetime.datetime.now()
            form.save()
            return redirect(home)
    else:
        form = UploadFileForm()
    return render(request, 'testfileapp/home.html', {
        'files': files,
        'upload_file_form': form,

    })


def sign_up(request):
    user_form = UserForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            User.objects.create_user(**user_form.cleaned_data)

            return redirect(home)

    return render(request, 'testfileapp/sign_up.html', {
        'user_form': user_form,
    })