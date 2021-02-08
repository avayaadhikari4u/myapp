from django.urls import path
from .views.login import Login,logout
from .views.signup import Signup
from .views.home import Index
from .views.cart import Cart
from .views import home
from .views.checkout import CheckOut
from .views.orders import Order
from .views.customer_profile import Customer_profile
urlpatterns = [
    path('',Index.as_view(),name='homepage'),
    path('empty/',home.emptycart,name='empty'),
    path('subcategory/',home.Subcategory,name='subcategory'),
    path('search/',home.search,name='search'),
    path('profil_prp/',home.profil_prp,name='profil_prp'),
    path('contact/',home.contact,name='contact'),
    path('signup/',Signup.as_view(),name='signup'),
    path('login/',Login.as_view(),name='login'),
    path('cart/',Cart.as_view(),name='cart'),
    path('logout/',logout,name='logout'),
    path('check-out',CheckOut.as_view(),name='checkout'),
    path('orders',Order.as_view(),name='orders'),
    path('customer_profile/',Customer_profile.as_view(),name='customerProfile'),
]