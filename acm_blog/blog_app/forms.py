from django import forms
from blog_app.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('author','title','text')

        # widgets={
        # 'title':forms.TextInput(attrs={'class':'textinputclass'}),
        # 'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        # }
