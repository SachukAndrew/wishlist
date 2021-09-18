from django.contrib import admin
from django.urls import path

from main.views import index, about, list_page

urlpatterns = [
    #path('URL adress', name_function)

    path('admin/', admin.site.urls),
    path('', index, name='index_page'),
    path('about/', about, name='about page'),
    path('wisher/<int:pk>/', list_page, name='wish_list_page'),
]
