from django.contrib.auth import mixins as auth_mixin
from django.views import generic as views

from library.lb_collections.forms import ItemCreateForm
from library.lb_collections.models import Item


class BookCreateView(auth_mixin.LoginRequiredMixin, views.CreateView):
    queryset = Item.objects.all()
    form_class = ItemCreateForm
    template_name = 'collections/item_create.html'
