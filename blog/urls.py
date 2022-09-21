
from django.urls import path,include
from .views import blog_posts

app_name = 'blog'
urlpatterns = [
# path('/', VIEW.as_view(), name=''),
path('blog-posts/', blog_posts, name='blog-posts'),
]
