from django.urls import path
from .views import home_view, article_list_view, article_detail_view

urlpatterns = [
    path('', home_view, name='home'),
    path('articles/', article_list_view, name='articles'),
    path('detail/<slug:slug>/', article_detail_view, name='detail'),
]
