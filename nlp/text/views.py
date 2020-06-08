from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import JsonResponse
from .forms import TextForm

def helloworld(request):
    """A test view which tells if the website is working."""
    return HttpResponse('hello world')

def index(request):
    """The only page of text app."""
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            return HttpResponse(handler(input_text=form.cleaned_data['text']))
    form = TextForm()
    context = {
        'form': form
    }
    return render(request, 'text/index.html', context)

def handler(input_text):
    """hook of text-handler"""
    result_text = f'hello world, the text is {input_text}'
    return result_text