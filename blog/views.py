from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import Profile
# Create your views here.


def home(request):
    context={
        'posts':Post.objects.all(),
        'title':'Home'
    }
    return render(request, 'blog/home.html',context)

class PostListView(ListView): 
    model=Post               #passes on objects to html file,object iterables are referred to as context_object_name
    template_name="blog/home.html"  #should be preferably - app/model_viewtype,html
    context_object_name='posts'   #matches name in html file
    ordering=["-date_posted"]


class PostDetailView(DetailView):
    model=Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    template_name='blog/post_form.html'   #not required, django automatically looks for app/model_form
    fields=['title','content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)# Call the base implementation first to get a context
        context['title'] = 'Create'
        return context

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model=Post
    template_name='blog/post_form.html'   #not required, django automatically looks for app/model_form
    fields=['title','content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)# Call the base implementation first to get a context
        context['title'] = 'Create'
        return context

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model=Post
    success_url='/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class UserPostListView(ListView): 
    model=Post               #passes on objects to html file,object iterables are referred to as context_object_name
    template_name="blog/user_posts.html"  #should be preferably - app/model_viewtype,html
    context_object_name='posts'   #matches name in html file


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)# Call the base implementation first to get a context
        context['context_author'] = get_object_or_404(User,username=self.kwargs.get('username'))
        return context
        
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('date_posted')
    
    

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})


