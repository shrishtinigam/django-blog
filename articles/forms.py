from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
    def clean(self):
        data = self.cleaned_data

        title = data.get('title')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', f'"{title}" is already in use.')
            
        return data


"""
class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == 'hello':
    #         raise forms.ValidationError('This title is blocked.')
    #     return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        # class = errorlist  -> ERROR IN FIELD ITSELF
        if title.lower().strip() == 'hello':
            self.add_error('title', 'This title is blocked.')
        
        # class = errorlist  -> ERROR IN FIELD ITSELF
        if content.lower().strip() == 'hello':
            self.add_error('content', 'This content is blocked.')

        # class = errorlist nonfield  -> ERROR IN ENTIRE FORM
        if 'hello' in content.lower() or 'hello' in title.lower():
            raise forms.ValidationError('Hello is not allowed in the article.')
        
        return cleaned_data
"""