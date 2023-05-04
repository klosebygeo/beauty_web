from django.urls import path

from homepage import views

urlpatterns = [
    path('',views.HomeTemplateView.as_view(), name ='homepage'),
]