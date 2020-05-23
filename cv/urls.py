from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_page, name='cv_page'),
    path('new/education', views.cv_new_education, name='cv_new_education')
]