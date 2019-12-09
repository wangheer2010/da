from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Format
from .forms import Form

def mainpage(request):
    form = Form()
    context = {'form':form,}
    return render(request,'NFL/list.html',context)


def offense(request):
    return render(request,'NFL/offense.html')

def defense(request):
    return render(request,'NFL/defense.html')

