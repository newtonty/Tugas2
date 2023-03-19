from django.urls import path, include

from main.views import *

urlpatterns = [
    path('', home, name='home'),
    path('study_tracker/', include('study_tracker.urls')),
]