from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from store.models.orders import Order
from django.views import View


# Create your views here.
class Index(View):
    def post(self, request):
        pass

    def get(self, request):
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
    # ToDo: Featured products
    """
      1. Products that are featured are best sales products selected randomly based on the order
      2. If nothing then get 3 products that are marked as best sale in product table
    """
    featured = Products.get_all_feature_products()

    # new product
    new_products = Products.get_new_product()

    # best sale
    best_sales = Products.get_best_sale_product()

    data = {
      "featured":featured,
      'new_products':new_products,
      'best_sales':best_sales,
    }
    return render(request, 'store/index.html', data)


