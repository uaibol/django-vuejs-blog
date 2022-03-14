from django.urls import path
from .views import post_create, post_detail

app_name = "posts"

urlpatterns = [
        path('create/', post_create, name='create'),
        path('<int:id>/', post_detail, name='detail'),
]
