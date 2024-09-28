from django import forms

from library.lb_events.models import Event


class EventBaseForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'date', 'location', 'description', 'age_group')


class EventCreateForm(EventBaseForm):
    pass
