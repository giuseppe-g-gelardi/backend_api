from django.urls import path
from cars import views

urlpatterns = [
    path('all/', views.get_all_cars),
    path('', views.user_cars),
]

# urlpatterns = [
#     path('', views.CarList.as_view())
# ]
