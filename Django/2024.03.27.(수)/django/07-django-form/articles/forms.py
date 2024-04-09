from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    summary = forms.CharField(
        widget=forms.CharField(
            arrts={
                'placeholder': 'summary'
            }
        )
    )
    memo = forms.Textarea(
        widget=forms.Textarea(
            arrts={
                'placeholder': 'memo',
                'cols': 50,
                'rows': 5
            }
        )
    )

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)