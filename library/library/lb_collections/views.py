from django.contrib.auth import mixins as auth_mixin
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework.utils import json

from library.lb_accounts.models import LibraryProfile
from library.lb_collections.forms import ItemCreateForm, ItemEditForm
from library.lb_collections.models import Item


class BookCreateView(auth_mixin.LoginRequiredMixin, views.CreateView):
    queryset = Item.objects.all()
    form_class = ItemCreateForm
    template_name = 'collections/item_create.html'
    success_url = reverse_lazy('item display')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user

        return form


def items_listed(request):
    context = {
        'items': Item.objects.all(),
    }

    return render(request, 'collections/item_display.html', context)


class ItemDetailView(views.DetailView):
    queryset = Item.objects.all()
    template_name = 'collections/item_detail.html'


class ItemEditView(views.UpdateView):
    queryset = Item.objects.all()
    template_name = 'collections/item_update.html'
    form_class = ItemEditForm
    success_url = reverse_lazy('item display')


@require_POST
def save_item_view(request, pk, slug):
    item = get_object_or_404(Item, pk=pk)  # Get the item based on the primary key
    user_profile = request.user.libraryprofile  # Access the user's profile

    # Toggle favorite status
    if item in user_profile.saved_items.all():
        user_profile.saved_items.remove(item)
        favorited = False
    else:
        user_profile.saved_items.add(item)
        favorited = True

    return JsonResponse({'favorited': favorited})