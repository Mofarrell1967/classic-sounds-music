from django.shortcuts import render, redirect, reverse
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import os

# Create your views here.


def contact(request):
    """A view that displays the index page"""
    return render(request, "contact.html")


def contact_message(request):
    """A view that displays the index page"""
    return render(request, "contact_message.html")


def send_email(request):
    name = request.POST.get('user_name')
    subject = request.POST.get('subject')
    message = request.POST.get('text')
    from_email = request.POST.get('user_email')
    the_message = " From: " + name + '\n' + " Email: " + \
        from_email + '\n' + " Message: " + message
    if subject and message and from_email:
        try:
            send_mail(subject, the_message, from_email,
                      [os.environ.get('EMAIL_ADDRESS')])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return render(request, 'contact_message.html')
    else:
        messages.error(request, "Please fill out all fields")

        return redirect(reverse('home'))
