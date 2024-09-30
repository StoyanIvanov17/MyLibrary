from django.urls import path, include

from library.lb_events import views

urlpatterns = [
    path('create/', views.EventCreateView.as_view(), name='event create'),
    path('display_events/', views.events_listed, name='event display'),
    path('<int:pk>/<slug:slug>/', include([
        path('detail/', views.EventDetailView.as_view(), name='event detail'),
        path('edit/', views.EventEditView.as_view(), name='event edit'),
        path('save_event/', views.save_event_view, name='save_event'),

    ]))
]
