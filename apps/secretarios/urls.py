from django.urls import path
from .views import home


# urls Alunos
urlpatterns = [
    path('home', home, name='home'),
]
