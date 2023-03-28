from django.urls import path
from study_tracker.views import *
from django.contrib.auth.decorators import login_required

app_name = 'study_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('create', create_assignment, name='create_assignment'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('modify/<int:id>', modify_assignment, name='modify_assignment'),
    path('delete/<int:id>', delete_assignment, name='delete_assignment'),
    path('create-ajax/', create_assignment_ajax, name='create_assignment_ajax'),
]
