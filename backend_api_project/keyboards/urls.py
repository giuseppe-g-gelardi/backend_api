from django.urls import path
from keyboards import views

urlpatterns = [
    path('all/', views.get_all_keyboards),
    path('', views.user_keyboards),
]
