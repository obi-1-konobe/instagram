from django import forms

from webapp.models import Post


class PostForm(forms.ModelForm):
    picture = forms.ImageField(
        required=True
    )

    class Meta:
        model = Post
        fields = ['picture', 'description']

