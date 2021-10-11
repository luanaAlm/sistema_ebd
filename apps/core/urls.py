from django.urls import path
from .views import index

# urls core
urlpatterns = [
    path('', index, name='index'),
]
