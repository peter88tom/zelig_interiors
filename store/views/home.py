from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from django.views import View


# Create your views here.
class Index(View):

    def post(self , request):
        pass

    def get(self , request):
        print(request.get_full_path())
        return HttpResponseRedirect(f'/home{request.get_full_path()[1:]}')


def home(request):
    # cart = request.session.get('cart')
    # if not cart:
    #     request.session['cart'] = {}
    # products = None
    # categories = Category.get_all_categories()
    # categoryID = request.GET.get('category')
    # if categoryID:
    #     products = Products.get_all_products_by_categoryid(categoryID)
    # else:
    #     products = Products.get_all_products()
    #
    # data = {}
    # data['products'] = products
    # data['categories'] = categories
    #
    # print('you are : ', request.session.get('email'))
    # #return render(request, 'store/index.html', data)
    return render(request, 'store/index.html')


