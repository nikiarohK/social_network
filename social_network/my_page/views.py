from django.shortcuts import render

def my_page(request):
    template = 'base.html'
    return render(request, template)
