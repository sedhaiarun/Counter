from cgitb import text
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   context = {
    'name' :'patrik',
    'age' : '50',
    'address':'sinamangal',
   }
   return render(request, 'index.html',context)

def counter(request):
    words= request.POST['text']
    amount_of_words= len(words.split())
    return render(request, 'counter.html', {'words': amount_of_words})
    