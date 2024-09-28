from django.urls import path, include

from library.lb_events import views

urlpatterns = [
    path('create/', views.EventCreateView.as_view(), name='event create'),
    path('<int:pk>/<slug:slug>/', include([
        path('details/', views.EventDetailView.as_view(), name='event detail'),
        path('edit/', views.EventEditView.as_view(), name='event edit'),
    ]))
]
