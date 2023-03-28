from django.urls import path, include

from main.views import *

urlpatterns = [
    path('', home, name='home'),
    path('tracker/', include('study_tracker.urls')),
]