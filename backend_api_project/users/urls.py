from django.urls import path
from users import views

urlpatterns = [
    path('all/', views.get_all_users),
    # path('', views.get_user),
    path('<int:id>/', views.get_user),
]