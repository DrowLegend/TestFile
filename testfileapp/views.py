import os


from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic.base import View
from django.http import JsonResponse, HttpResponse

from testfileapp.models import UploadFile
from django.contrib.auth.decorators import login_required
from testfileapp.forms import UserForm, UploadFileForm
from celery import current_app
from .tasks import set_status_as_inactive
from celery.result import AsyncResult
import time

# Create your views here.


def red(request):
    return redirect(home)


def home(request):
    files = UploadFile.objects.all()

    if request.method == 'POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)

        if upload_file_form.is_valid():
            upload_file_form.save()
            return redirect(home)
    else:
        upload_file_form = UploadFileForm()
    return render(request, 'testfileapp/home.html', {
        'files': files,
        'upload_file_form': upload_file_form,
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


# def run_task(request):
#     task = sum2.delay(6, 6)
#     current_app.AsyncResult(task.id)
#     task.get()
#     result = task.status
#     return render(request, 'testfileapp/home.html', {
#         'result': result
#     })