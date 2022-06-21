from django.contrib import admin
from django.urls import path
from .views.home import Index, home
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views.my_account import my_account
from .views.shop import shop_index
from .views.contact import IndexContact
from .views.item import ProductDetails


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('home', home, name='home'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),

    path("my-account", my_account, name='my-account'),
    path("shop", shop_index.as_view(), name="shop"),
    path("shop/item/<str:slug_details>", ProductDetails.as_view()),
    path("contact", IndexContact.as_view(), name="contact"),


]
