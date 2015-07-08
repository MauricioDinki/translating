from django import forms

from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['name', 'category', 'author', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 20, 'rows': 10, 'class': 'materialize-textarea'}),
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(BookForm, self).clean()
        return cleaned_data
