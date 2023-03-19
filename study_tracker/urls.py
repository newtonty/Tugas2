from django.urls import path
from study_tracker.views import show_tracker
from study_tracker.views import create_assignment
from study_tracker.views import show_xml
from study_tracker.views import show_json
from study_tracker.views import show_xml_by_id, show_json_by_id
from study_tracker.views import register #sesuaikan dengan nama fungsi yang dibuat
from study_tracker.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from study_tracker.views import logout_user
from django.contrib.auth.decorators import login_required
from study_tracker.views import modify_assignment
from study_tracker.views import delete_assignment



app_name = 'study_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('create', create_assignment, name='create_assignment'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('modify/<int:id>', modify_assignment, name='modify_assignment'),
    path('delete/<int:id>', delete_assignment, name='delete_assignment'),
]
