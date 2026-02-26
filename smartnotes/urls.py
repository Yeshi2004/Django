from django.urls import path
from . import views


app_name = "smartnotes"

urlpatterns = [
    path('', views.smart_notes, name='home'),
    path('delete/<int:note_id>/', views.delete_note, name='delete'),
]