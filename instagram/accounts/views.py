from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, UpdateView

from accounts.forms import UserCreationForm, UserChangeForm
from webapp.models import Post


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('webapp:index')
    else:
        form = UserCreationForm()
    return render(request, 'create_user.html', context={'form': form})


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.pictures.all()
        return context


class UserPersonalInfoChangeView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_info_change.html'
    form_class = UserChangeForm
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']


def subscribe_to_user(request, **kwargs):
    user = request.user
    subscribe_to = User.objects.get(pk=kwargs['pk'])

    subscribe_to.profile.subscriber.add(user)
    return redirect(request.META.get('HTTP_REFERER'))
