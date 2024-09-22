from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from library.lb_collections import views

urlpatterns = [
    path('create/', views.BookCreateView.as_view(), name='item create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
