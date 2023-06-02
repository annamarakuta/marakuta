from django.shortcuts import get_object_or_404, render
from django.db.models import Q
import datetime

from blog.models import Post
from blog.models import Category


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.filter(
        Q(is_published=True) &
        Q(category__is_published=True) &
        Q(pub_date__lte=datetime.datetime.now())
    ).order_by('-pub_date')[0:5]
    context = {
        'post_list': post_list,
    }
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.filter(
        Q(is_published=True) &
        Q(category__is_published=True) &
        Q(pub_date__lte=datetime.datetime.now())
        ),
        id=id
    )
    context = {
        'post': post,
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'

    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=category_slug
    )

    post_list = Post.objects.filter(
        Q(is_published=True) &
        Q(category__slug=category_slug) &
        Q(pub_date__lte=datetime.datetime.now())
    )

    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template_name, context)
