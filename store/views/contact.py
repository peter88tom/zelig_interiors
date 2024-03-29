from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.conf import settings
from django.core.mail import send_mail
from store.models.contact import Contact



class IndexContact(View):
    def post(self, request):
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')
        subject = request.POST.get('title')

        # Send email here
        subject = f"Qoute: {subject} From {name}"
        message = message
        email_from = email
        recipient_list = [settings.EMAIL_HOST_USER,]

        try:
          contact = Contact.objects.get()
        except Contact.DoesNotExist:
          contact = {}

        try:
          send_mail(subject, message, email_from, recipient_list)
          data = {
            "msg": "Thank you for your email, We will get back to as soon as possible",
            "status": "success",
            'contact_info': contact
          }
        except Exception as e:
            print(e)
            data = {
              "msg": "Something went wrong could not send email, Please use contact below to reach us",
              "status":"danger",
              'contact_info': contact
            }

        return render(request, 'store/contact.html', data)

    def get(self, request):
        try:
          contact = Contact.objects.get()
        except Contact.DoesNotExist:
          contact = {}
        data = {
          'contact_info': contact
        }
        return render(request, 'store/contact.html', data)


def get_contact(request):
  try:
    g_contact = Contact.objects.get()
  except Contact.DoesNotExist:
    g_contact = {}

  return {
    "contact_details": g_contact,
  }
