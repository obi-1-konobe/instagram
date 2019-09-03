from django.views.generic import ListView

from webapp.models import Post


class IndexView(ListView):
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')
    

