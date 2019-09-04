from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from webapp.forms import PostForm, CommentForm
from webapp.models import Post


class IndexView(ListView):
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('-created_at')
        context['form'] = CommentForm
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




