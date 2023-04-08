from django.shortcuts import render

# Create your views here.

def com_home(request):
    return render(request,'common/home.html')
def com_about(request):
    return render(request,'common/about.html')
def com_ourbrand(request):
    return render(request,'common/ourbrands.html')
def com_jell(request):
    return render(request,'common/jewellery.html')
def com_con(request):
    return render(request,'common/contact.html')