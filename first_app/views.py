from django.shortcuts import render
from . import forms
# Create your views here.
def home(request):
    form = forms.TestForm()
    return render(request, 'output.html', {'form': form})
