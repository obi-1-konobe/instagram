from django.views.generic import ListView, DetailView

from webapp.models import Post


class IndexView(ListView):
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'



