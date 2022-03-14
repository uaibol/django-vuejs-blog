from django.urls import path, include
from .views import PostList, PostDetail, CommentList

app_name = "api"

urlpatterns = [
        path('<int:pk>/', PostDetail.as_view()),
        path('comments/', CommentList.as_view()),
        path('', PostList.as_view()),
        #path('', post_list_create_api_view, name='postlist'),
        path('api-auth/', include('rest_framework.urls')), # new
]
