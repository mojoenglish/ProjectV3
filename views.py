from django.shortcuts import render

def home(request):
  message = "Welcome to my website!"
  return render(request, 'welcomeapp/home.html', {'message': message})

from django.shortcuts import render
from django.http import HttpResponseRedirect  # Added for handling form submission

def contact(request):
  if request.method == 'POST':
    
    name = request.POST.get('name')  # Access form data by key
    email = request.POST.get('email')
    message = request.POST.get('message')

  
    

    
    if name and email and message:
      # Form is valid, process data 
      processed = True
      message = "Thanks for contacting us, " + name + "!"
    else:
      # Form is invalid, display error message
      processed = False
      message = "Please fill out all required fields."

    # Redirect to the same page after processing (optional)
    if processed:
      return HttpResponseRedirect('/contact/')  # Redirect to contact page after successful processing

  else:
    message = "Fill out the form below:"
  return render(request, 'welcomeapp/contact.html', {'message': message})
