from django.shortcuts import render

# Create your views here.
def index(request): #este index llamo en urls.py de cliente
    
    return render(request,'cliente/indexBefine.html') #dirección de donde esta mi index