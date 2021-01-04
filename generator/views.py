from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator_appname/home.html')

def password(request):
    characters=list('abcdefghijklmnopqrstuvwxyz')
    thepassword =''
    if (request.GET.get('uppercase')):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if (request.GET.get('numbers')):
        characters.extend(list('1234567890'))

    if (request.GET.get('specialcharacters')):
        characters.extend(list('=+-_!@#$%^&*(~``)'))
    length =int(request.GET.get('length',12))
    for x in range (length):
        thepassword+=random.choice(characters)
    return render(request,'generator_appname/password.html',{'password':thepassword})

def about(request):
        return render(request,'generator_appname/about.html')
