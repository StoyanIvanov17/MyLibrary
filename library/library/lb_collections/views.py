from django.contrib.auth import mixins as auth_mixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework.utils import json

from library.lb_accounts.models import LibraryProfile
from library.lb_collections.forms import ItemCreateForm, ItemEditForm, ReviewForm
from library.lb_collections.models import Item, Reviews


class BookCreateView(auth_mixin.LoginRequiredMixin, views.CreateView):
    queryset = Item.objects.all()
    form_class = ItemCreateForm
    template_name = 'collections/item_create.html'
    success_url = reverse_lazy('item display')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user

        return form


class ItemListView(views.ListView):
    template_name = 'collections/item_display.html'
    context_object_name = 'items'

    def filter_by_genre(self, queryset):
        genre_query = self.request.GET.get('genre', '')

        if genre_query:
            return Item.objects.filter(genre__icontains=genre_query)

        return queryset

    def get_queryset(self):
        queryset = Item.objects.all()
        return self.filter_by_genre(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre_query'] = self.request.GET.get('genre', '')

        return context


class ItemDetailView(views.DetailView):
    queryset = Item.objects.all()
    template_name = 'collections/item_detail.html'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = self.form_class()
        context['reviews'] = Reviews.objects.filter(item=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        item = self.get_object()
        form = self.form_class(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.item = item
            review.user = request.user
            review.save()
            return JsonResponse({
                'success': True,
                'review_text': review.comment,
                'username': request.user.libraryprofile.full_name,
                'created_at': review.created_at.strftime('%Y-%m-%d %H:%M:%S')
            })
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)


class ItemEditView(views.UpdateView):
    queryset = Item.objects.all()
    template_name = 'collections/item_update.html'
    form_class = ItemEditForm
    success_url = reverse_lazy('item display')


class ItemDeleteView(views.DeleteView):
    queryset = Item.objects.all()
    success_url = reverse_lazy('item display')


@require_POST
def save_item_view(request, pk, slug):
    item = get_object_or_404(Item, pk=pk)
    user_profile = request.user.libraryprofile

    if item in user_profile.saved_items.all():
        user_profile.saved_items.remove(item)
        favorited = False
    else:
        user_profile.saved_items.add(item)
        favorited = True

    return JsonResponse({'favorited': favorited})
