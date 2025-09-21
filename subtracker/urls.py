from django.contrib import admin        # ← this imports admin
from django.urls import path, include
from django.views.generic import RedirectView  # optional, if you want to redirect root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subscriptions/', include('subscriptions.urls')),
    path('', RedirectView.as_view(url='/subscriptions/')),  # optional root redirect
]
