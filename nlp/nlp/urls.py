from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('text/', include('text.urls')),
    path('', RedirectView.as_view(url='text/'), name='index'),
]
