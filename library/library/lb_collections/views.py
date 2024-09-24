from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from library.lb_collections.forms import ItemCreateForm, ItemEditForm
from library.lb_collections.models import Item


class BookCreateView(auth_mixin.LoginRequiredMixin, views.CreateView):
    queryset = Item.objects.all()
    form_class = ItemCreateForm
    template_name = 'collections/item_create.html'
    success_url = reverse_lazy('item collection')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user

        return form


def items_listed(request):
    context = {
        'items': Item.objects.all(),
    }

    return render(request, 'collections/items_listed.html', context)


class ItemDetailView(auth_mixin.LoginRequiredMixin, views.DetailView):
    queryset = Item.objects.all()
    template_name = 'collections/item_detail.html'


class ItemEditView(views.UpdateView):
    queryset = Item.objects.all()
    template_name = 'collections/item_edit.html'
    form_class = ItemEditForm
    success_url = reverse_lazy('item collection')

