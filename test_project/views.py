from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render (request , 'home.html')

def test(request):
    return render (request , 'index.html')
def onama(request):
    return render (request , 'onama.html')
def usluge(request):
    return render (request , 'usluge.html')
def galerija(request):
    return render (request , 'galerija.html')
def kontakt(request):
    return render (request , 'kontakt.html')

def pitanje(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            subject=form.cleaned_data['subject']
            phone=form.cleaned_data['phone']
            message=form.cleaned_data['message']
            

            html=render_to_string('contact.html', {
                'name': name,
                'email': email,
                'subject': subject,
                'phone': phone,
                'message': message })
            
        send_mail('Subjekt',html,email,['TvojaStranica@com.com'],html_message=html)
        
        

        return redirect('pitanje')
    else:
        form = ContactForm()

    return render(request, 'pitanje.html', {'form': form})

