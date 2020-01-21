from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
from django.contrib import messages

def index(request):
	return render(request, 'core/index.html')

def contact_us(request):
	contact_form = ContactForm(request.POST or None)
	context={
		'form': contact_form  
	}
	if request.method == 'POST':
		
		if contact_form.is_valid():
			r_name = request.POST.get('name')
			r_email = request.POST.get('email')
			r_message = request.POST.get('message')
			c= Contact(name = r_name, email = r_email, message = r_message)
			c.save()

			messages.success(request, f'Your messsage was sent. We will get to you as soon as possible.')
			return render(request, 'core/contact_us.html', {'form': ContactForm()})

		else:
			form = ContactForm()
		messages.warning(request, f"Your messsage was not sent. Please try again.")
	return render(request, 'core/contact_us.html',context )

def course(request):
	return render(request, 'core/course.html')

def about_us(request):
	return render(request, 'core/about_us.html')