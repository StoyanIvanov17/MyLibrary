from django import forms

from library.lb_collections.models import Item, Author


class ItemBaseForm(forms.ModelForm):
    author = forms.CharField(
        max_length=Author.MAX_NAME_LENGTH,
        widget=forms.TextInput(attrs={'placeholder': 'Author'})
    )

    class Meta:
        model = Item
        fields = ['title', 'author', 'genre', 'item_type', 'publication_date', 'isbn', 'item_image']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author'}),
            'genre': forms.TextInput(attrs={'placeholder': 'Genre'}),
            'item_type': forms.Select(attrs={'placeholder': 'Item Type'}),
            'publication_date': forms.DateInput(attrs={'placeholder': 'Publication Date', 'type': 'date'}),
            'isbn': forms.TextInput(attrs={'placeholder': 'ISBN'}),
            'item_image': forms.FileInput(attrs={'placeholder': 'Item Image'}),
        }

    def clean_author(self):
        author_name = self.cleaned_data['author']
        author, created = Author.objects.get_or_create(name=author_name)

        return author

    def save(self, commit=True):
        return super().save(commit=commit)


class ItemCreateForm(ItemBaseForm):
    pass


class ItemEditForm(ItemBaseForm):
    pass
