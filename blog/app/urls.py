from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id>', views.postDetail, name='postDetail'),
    path('form/', views.form, name='form'),
]
