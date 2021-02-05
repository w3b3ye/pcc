"""Defines URL patterns for app_learning_logs"""

from django.urls import path
from . import views

app_name = 'app_learning_logs'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    #Detail page for single topic.
    path('topics/<int:topic_id>', views.topic, name='topic'),
]