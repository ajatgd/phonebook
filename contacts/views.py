from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework import generics
from .forms import *
from django.db.models import Q
from django.contrib import messages
from django.db import IntegrityError
# Create your views here.


def index(request):
    return render(request, 'index.html')


def fillDetails(request):

    if request.method == "POST":
        try:
            form = PhonebookForm(request.POST)
            if form.is_valid():
                post = form.save()
                post.save()
                messages.success(request, 'Form submission successful')
                return render(request,'index.html')
        except IntegrityError as e:
            return render(request,'index.html')
        except:
            return render(request,'index.html')
    else:
        form = PhonebookForm()
        return render(request, 'fillDetails.html', {'form': form})
