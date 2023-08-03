from django.urls import path
from mypro import views

app_name="mypro"
urlpatterns = [
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('blog_single', views.blog_single, name='blog_single'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('index', views.index, name='index'),
    path('portfolio', views.portfolio, name='portfolio'),
    


    path('base', views.base, name = 'base'),
    path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login_reg'),
    path('logout', views.logoutuser, name = 'logout'),

    path('product', views.product, name='product'),
    path('products', views.products, name='products'),
    path('order/<int:id>', views.order, name='order'),
    path('kart', views.kart  , name='kart '),
   
]