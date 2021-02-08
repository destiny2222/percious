from django.shortcuts import render, redirect
from django.http import  HttpResponse
from django.core.mail import send_mail
from percious.settings import EMAIL_HOST_USER
from .forms import ContactForm
from .models import * 
# Create your views here.
def indexpage (request):
	  qs = home.objects.all().filter(category='AP')
	  QP = home.objects.all().filter(category='CL')
	  qw = home.objects.all().filter(category='ST')
	  QR = home.objects.all().filter(category='GA')
	  context = {
	  'about': qs,
      'class': QP,
      'staff': qw,
      'gallery': QR,
	  }
	  return render(request, 'index/index.html', context)


def aboutpage(request):
	qs = home.objects.filter(category='AP')
	qw = home.objects.all().filter(category='ST')
	qv = home.objects.all().filter(category='SL')
	context = {
	'about': qs,
    'staff': qw,
    'silder': qv,
	}
	return render(request,'index/about.html', context)


def contactpage(request):
    form_class = ContactForm
    form = form_class(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            Subject = request.POST['subject']
            message = request.POST['message']
            send_mail(subject,message,email,name, ['perciouskid@gmail.com'],fail_silently=False,)
            return Redirect('successes')
    return render(request, 'index/contact.html',{'form': form})	
                          



def success(request):
    return render(request,'index/success.html')