from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('menu',views.menu,name="menu"),
    path('search',views.search,name="search"),
    path('login',views.login_view,name="login"),
    path('logout',views.logout_view,name="logout"),
    path('create',views.create,name="create"),
    path('cart',views.cart,name="cart"),
    path('save_order',views.save_order,name="save_order"),
    path('cart',views.cart_view,name="cart_view"),
]
