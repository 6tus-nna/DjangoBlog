from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, AddCommentView,AddReplyView,UpdatePostView,LikeView,DeletePostView, AddCategoryView,CategoryPost, CategoryList


app_name = 'blog'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', PostDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete/', DeletePostView.as_view(), name="delete-post"),
    path('category/<str:cats>/', CategoryPost, name='category'),
    path('categort_menu',CategoryList, name='category-menu' ),
    path('like/<int:pk>/', LikeView, name='like_post'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
    path('article/comment/<int:pk>/reply/', AddReplyView.as_view(), name='add_reply'),
    
   
]