from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'store/login_registration.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        print(customer)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                message = 'Invalid email or password'
                message_status = 'danger'
        else:
            message = 'Invalid email or password'
            message_status = 'danger'

        print (email, password)
        return render(request, 'store/login_registration.html', {'msg': message, 'status': message_status})


def logout(request):
    request.session.clear()
    return redirect('login')
