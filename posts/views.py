from django.shortcuts import render, get_object_or_404
from .models import Post
# Django REST Framework
from rest_framework import generics
from .serializers import PostSerializer

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-fecha_publicacion')
    template = 'posts/post_list.html'
    context = {
        'posts': posts
    }
    return render(request, template, context)   


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    template = 'posts/post_detail.html'
    context = {
        'post': post
    }
    return render(request, template, context)



# ------- Vistas para usar DRF usando las clases genericas ----------
class PostListAPIView(generics.ListCreateAPIView):
    """ 
    Esta clase ya contiene los metodos GET y POST
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Esta clase ya contiene los metodos GET, PUT y DELETE
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer