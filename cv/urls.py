from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_page, name='cv_page'),
    path('new/education', views.cv_new_education, name='cv_new_education'),
    path('new/skill', views.cv_new_skill, name='cv_new_skill'),
    path('new/experience', views.cv_new_experience, name='cv_new_experience'),
    path('new/project', views.cv_new_project, name='cv_new_project'),
    path('remove/education/<int:pk>', views.cv_remove_education, name='cv_remove_education'),
]