from django.contrib.auth.models import User
from django.views.generic import TemplateView

from webapp.forms import SearchForm


class SearchView(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, *args, **kwargs):
        form = SearchForm
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('search')
        if query:
            results = set()

            search_username = User.objects.filter(username__icontains=query)
            for user in search_username:
                results.add(user)

            search_email = User.objects.filter(email__icontains=query)
            for user in search_email:
                results.add(user)

            search_name = User.objects.filter(first_name__icontains=query)
            for user in search_name:
                results.add(user)

            search_about_me = User.objects.filter(profile__about_me__icontains=query)
            for user in search_about_me:
                results.add(user)

            context['results'] = results

        context['search_form'] = form
        return context
