from django.shortcuts import render

from .models import Precatory

# Create your views here.


def index(request):
    precatory_list = Precatory.objects.all()
    return render(request, 'index.html', {'precatory_list': precatory_list})