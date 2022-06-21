from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from django.views import View


class ProductDetails(View):
    def post(self, request, slug_details):
      pass
    def get(self, request, slug_details):
      cart = request.session.get('cart')
      if not cart:
        request.session['cart'] = {}

      categories = Category.get_all_categories()
      products = Products.get_products_by_slug_name(slug_details)

      data = {}

      data['products'] = products
      data['categories'] = categories

      return render(request, 'store/product_details.html', data)
