from django.urls import path
from .views import BlogView, ArticleDetailView

urlpatterns = [
    path('', BlogView.as_view(), name="blog"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail')
]
