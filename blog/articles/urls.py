from django.urls import path
from articles import views


urlpatterns = [
    path('', views.index, name='articles.index'),
    path('<int:id>/', views.show, name='articles.show'),
]
