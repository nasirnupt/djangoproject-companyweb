from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from.models import Blog, recentpost

# Create your views here.
def blog(request):
    blog_data = Blog.objects.all()
    recentpost_data = recentpost.objects.order_by('-publish_date')

    paginator = Paginator(blog_data, 3)
    page_number = request.GET.get('page')
    paged_obj = paginator.get_page(page_number)

    context ={
        'blogs':paged_obj,
        'recentposts':recentpost_data,
    }
    return render(request, 'blog/blog.html', context)

def search(request):
    queryset_list = Blog.objects.order_by('-publish_date')

    # Keywords Filtering
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords)

    context={
        'blogs':queryset_list,
        'values': request.GET,
    }
    return render(request, 'blog/search.html', context)

def singleblog(request):
    return render(request, 'blog/singleblog.html')
