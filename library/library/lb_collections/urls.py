from django.urls import path, include

from library.lb_collections import views

urlpatterns = [
    path('create/', views.BookCreateView.as_view(), name='item create'),
    path('display_items/', views.items_listed, name='item display'),
    path('<int:pk>/<slug:slug>/', include([
        path('detail/', views.ItemDetailView.as_view(), name='item detail'),
        path('edit/', views.ItemEditView.as_view(), name='item edit'),
        path('delete/', views.ItemDeleteView.as_view(), name='item delete'),
        path('save_item/', views.save_item_view, name='save_item'),
    ])),
]
