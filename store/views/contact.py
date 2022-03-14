from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.contact import Contact
from django.views import View


class IndexContact(View):
    def post(self, request):
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')
        print(email)
        print(name)
        print(message)

        # Send email here

        message = 'Thank you, We will come back to you with response soon'
        message_status = 'success'
        return render(request, 'store/contact.html', {'msg': message, 'status': message_status})

    def get(self, request):
        contact = Contact.objects.get()
        data = {
          'contact_info': contact
        }
        return render(request, 'store/contact.html', data)


def contact(request):
    pass
