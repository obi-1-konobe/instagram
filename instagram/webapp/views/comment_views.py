from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import CommentForm
from webapp.models import Post, Comment


class CommentCreateView(CreateView):
    form_class = CommentForm

    def form_valid(self, form):
        post = Post.objects.get(pk=self.kwargs.get('pk'))

        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.kwargs.get('pk')})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)