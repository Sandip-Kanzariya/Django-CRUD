from django.urls import path
from . import views
urlpatterns = [
    path('', views.products, name='products'),
    path('create', views.create_product, name='create_product'),
    path('update/<int:pk>', views.update_product, name="update_product"),
    path('delete/<int:pk>', views.delete_product, name="delete_product"),
]