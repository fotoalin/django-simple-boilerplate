from django.shortcuts import render, redirect


def index_page(request):
    return redirect('home_page')



def home_page(request):
    return render(request, 'testapp/index.html')