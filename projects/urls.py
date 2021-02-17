from django.urls import path
from . import views


"""
Here, we create URL Conf. The urlpatterns map each request path to the relevant view.
"""
urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]