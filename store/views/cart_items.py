from store.models.product import Products


def get(request):
    cart = request.session.get('cart')
    if not cart:
      request.session['cart'] = {}
    ids = list(request.session.get('cart').keys())
    products = Products.get_products_by_id(ids)
    print(products)
    return {
      "cart_items": products,
    }

