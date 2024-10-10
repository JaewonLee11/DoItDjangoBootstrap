from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


#
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'post_list' : posts
#         }
#     )

# ---->

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    # 혹은 ListlView 클래스는 _list.html를 자동으로 인식하므로 index.html의 이름을 post_list.html로 변경



#
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post' : post,
#         }
#
#     )

# ---->

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/single_post_page.html'
    # 혹은 DetailView 클래스는 _detail.html를 자동으로 인식하므로 single_post_page.html의 이름을 post_detail.html로 변경


# Create your views here.
