from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="home-page"),
    path('add_user_information', views.post_new_user_information, name="add-user-info"),
]
