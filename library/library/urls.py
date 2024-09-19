from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('library.lb_home.urls')),
    path('accounts/', include('library.lb_accounts.urls')),
    path('collections/', include('library.lb_collections.urls')),
    path('events/', include('library.lb_events.urls')),
]
