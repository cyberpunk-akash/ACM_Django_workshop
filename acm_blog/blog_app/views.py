from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from blog_app.forms import PostForm
from blog_app.models import Post
# Create your views here.


def index(request):
    # return HttpResponse("Hello world")
    return render(request,'blog_app/index.html')


# class CreatePostView(CreateView):
#     template_name='blog_app/blog_form.html'
#     redirect_field_name='blog_app/blog_detail.html'
#     form_class=PostForm
#     model=Post

def form_name_view(request):
    form=PostForm()
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # return index(request)
        else:
            print('Error')

    return render(request, 'blog_app/blog_form.html',{'form':form})


class PostListView(ListView):
    model=Post
    template_name='blog_app/blog_detail.html'
