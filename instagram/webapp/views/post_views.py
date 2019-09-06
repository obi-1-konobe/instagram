from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from webapp.forms import PostForm, CommentForm, SearchForm
from webapp.models import Post


class IndexView(ListView):
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm
        context['form'] = CommentForm
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('-created_at')
        context['form'] = CommentForm
        context['likes'] = len(self.object.users_like.all())

        return context


class PostCreateView(CreateView):
    template_name = 'posts/post_create.html'
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


def put_likes(request, **kwargs):
    user = request.user
    post = Post.objects.get(pk=kwargs['pk'])

    if user in post.users_like.all():
        post.users_like.remove(user)
    else:
        post.users_like.add(user)

    return redirect(request.META.get('HTTP_REFERER'))




