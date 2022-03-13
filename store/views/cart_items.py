from store.models.product import Products


def get(request):
    ids = list(request.session.get('cart').keys())
    products = Products.get_products_by_id(ids)
    print(products)
    return {
      "cart_items": products,
    }

