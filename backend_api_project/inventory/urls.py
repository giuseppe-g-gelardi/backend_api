from django.urls import path
from inventory import views

urlpatterns = [
    path('all/', views.InventoryList.as_view()),
    path('<int:pk>/', views.InventoryDetail.as_view())
]
