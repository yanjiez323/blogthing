from django.shortcuts import render
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})
