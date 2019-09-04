from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, UpdateView

from accounts.forms import UserCreationForm, UserChangeForm
from accounts.models import Profile
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
        context['subscribers'] = len(self.object.profile.subscriber.all())
        context['subscribe_to'] = len(self.object.profile.subscribe_to.all())

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
    subscriber_profile = Profile.objects.get(user=request.user.pk)
    user_profile = Profile.objects.get(user=kwargs['pk'])

    if subscriber_profile in user_profile.subscriber.all():
        subscriber_profile.subscribe_to.remove(user_profile)
    else:
        subscriber_profile.subscribe_to.add(user_profile)

    return redirect(request.META.get('HTTP_REFERER'))
