from django.shortcuts import render , redirect
from .models import Post
from .forms import PostForm


def post_list (request):
    data = Post.objects.all() # 1-model : query
    return render(request,'posts_list.html', {'posts':data}) # 2-template : frontend   3-context {}




from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
class PostList(ListView):
    model = Post    # 1-model : query   2-post_list.html   3-post_list


class PostDetail(DetailView):
    model = Post   # context:post


class PostCreate(CreateView):
    model = Post
    # fields = '__all__'
    success_url='/blog/'
    form_class = PostForm

class PostEdit(UpdateView):
    model = Post
    # fields = '__all__'
    success_url='/blog/'
    template_name = 'posts/edit_post.html'
    form_class = PostForm


class PostDelete(DeleteView):
    model = Post
    success_url='/blog/'