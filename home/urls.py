from django.urls import path
from . import views


"""
Here, we create URL Conf. The urlpatterns map each request path to the relevant view.
"""
urlpatterns = [
    path('', views.BioList.as_view()),
]