from django.shortcuts import render
from django.views import generic  # this is to add generic library
from .models import Post  # this is to add Post class

# Create your views here.


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
