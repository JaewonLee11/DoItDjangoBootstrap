from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index), ->
    path('', views.PostListView.as_view()),
    # path('<int:pk>/', views.single_post_page), ->
    path('<int:pk>/', views.PostDetailView.as_view()),

]