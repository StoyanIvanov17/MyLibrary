from django.urls import reverse
from django.views import generic as views

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