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

        # Send email here
        subject = f"Zelig Interiors Form Send By {name}"
        message = message
        email_from = email
        recipient_list = [settings.EMAIL_HOST_USER,]

        contact = Contact.objects.get()

        try:
          send_mail(subject, message, email_from, recipient_list)
          data = {
            "msg": "Thank you for your email, Will will revert back to as soon as possible",
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
        contact = Contact.objects.get()
        data = {
          'contact_info': contact
        }
        return render(request, 'store/contact.html', data)


def contact(request):
    pass
