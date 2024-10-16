from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import generic as views
from django.views.decorators.http import require_POST

from library.lb_events.forms import EventCreateForm
from library.lb_events.models import Event


class EventCreateView(views.CreateView):
    queryset = Event.objects.all()
    form_class = EventCreateForm
    template_name = 'events/event_create.html'

    def get_success_url(self):
        return reverse('event detail', kwargs={
            'pk': self.object.pk,
            'slug': self.object.slug
        })

    # for association with the user
    def get_form(self, form_class=form_class):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user
        return form


def events_listed(request):
    events = Event.objects.all()
    current_datetime = timezone.now()
    filter_option = request.GET.get('filter', '')

    if filter_option == 'upcoming':
        events = events.filter(date__gte=current_datetime)

    context = {
        'events': events,
        'filter_upcoming': filter_option,
    }

    return render(request, 'events/event_display.html', context)


class EventDetailView(views.DetailView):
    queryset = Event.objects.all()
    template_name = 'events/event_detail.html'


class EventEditView(views.UpdateView):
    queryset = Event.objects.all()
    template_name = 'events/event_update.html'
    form_class = EventCreateForm

    def get_success_url(self):
        return reverse('event detail', kwargs={
            'pk': self.object.pk,
            'slug': self.object.slug
        })


class EventDeleteView(views.DeleteView):
    queryset = Event.objects.all()
    success_url = reverse_lazy('event display')


@require_POST
def save_event_view(request, pk, slug):
    event = get_object_or_404(Event, pk=pk)
    user_profile = request.user.libraryprofile

    # Toggle favorite status
    if event in user_profile.saved_events.all():
        user_profile.saved_events.remove(event)
        favorited = False
    else:
        user_profile.saved_events.add(event)
        favorited = True

    return JsonResponse({'favorited': favorited})