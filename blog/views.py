from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import CommentForm, PostForm
from .models import Post, Comment
from django.views.generic.edit import DeleteView, UpdateView

def post_new(request):
    
    form = PostForm()

    if request.method == "POST":

        form = PostForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit=False)

            post.author = request.user

            post.save()

            return redirect('post_list')

    context = {

        'form' : form
    }

    return render(request, 'blog/post_new.html', context)

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post)
    # form = PostDetailForm(request.POST)
    commentform = CommentForm()

    if request.method == 'POST':
        commentform = CommentForm(request.POST or None)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('home')
            
    return render(request, 'blog/post_detail.html', {'post':post,  'commentform' : commentform, 'comments' : comments})
    

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_detail.html'
    success_url = reverse_lazy('home')

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('home')
    form_class = PostForm


