from django.urls import path
from . import views


urlpatterns = [
    # path()
    path('',views.loginPage, name='home'),
    path('products/',views.products),
    path('customers/',views.customers),
    path('register/',views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),

]
