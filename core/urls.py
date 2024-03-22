from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path("", views.home, name="home"),
    # Add Tasks
    path("addTask/", views.addTask, name="addTask"),
    # Mark is Done Tasks
    path("mark_as_done/<int:pk>/", views.mark_as_done, name="mark_as_done"),
    # Mark is UnDone Tasks
    path("mark_as_undone/<int:pk>/", views.mark_as_undone, name="mark_as_undone"),
    # Edit Tasks
    path("edit_Task/<int:pk>/", views.edit_Task, name="edit_Task"),
    # Delete Tasks
    path("delete_Task/<int:pk>/", views.delete_Task, name="delete_Task"),
]
