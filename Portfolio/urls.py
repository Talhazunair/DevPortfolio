from . import views
from django.urls import path
urlpatterns = [
    path('',views.index,name="home"),
    path('skill',views.skill,name='skill'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('project',views.project,name='project'),
    path('projectdetail/<int:id>',views.projectdetail,name='projectdetail'),
]
