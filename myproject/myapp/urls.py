from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('selection.html', views.selection, name='selection'),
    path('ginput.html', views.input, name='input'),
    path('tracker.html', views.tracker, name='tracker'),
    path('Output.html', views.output, name='output'),
    path('newabout.html', views.about, name='about'),
    path('fancycontact.html', views.contact, name='contact')
    ]