from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .constants import POSTS_COUNT
from .models import Category, Post


def get_published_posts():
    return Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    )


def index(request):
    posts = get_published_posts()[:POSTS_COUNT]
    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    post = get_object_or_404(
        get_published_posts(),
        pk=id,
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    posts = category.posts.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
    )
    context = {
        'category': category,
        'post_list': posts,
    }
    return render(request, 'blog/category.html', context)
