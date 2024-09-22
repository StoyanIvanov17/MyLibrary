from django import forms

from library.lb_collections.models import Item


class ItemBaseForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'author', 'genre', 'item_type', 'publication_date', 'isbn']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author'}),
            'genre': forms.TextInput(attrs={'placeholder': 'Genre'}),
            'item_type': forms.Select(attrs={'placeholder': 'Item Type'}),
            'publication_date': forms.DateInput(attrs={'placeholder': 'Publication Date', 'type': 'date'}),
            'isbn': forms.TextInput(attrs={'placeholder': 'ISBN'}),
        }


class ItemCreateForm(ItemBaseForm):
    pass
