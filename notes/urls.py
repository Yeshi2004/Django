from django.urls import path
from . import views

urlpatterns=[
    path('',views.smart_notes, name='smart_notes'),
    path('create/', views.create_note, name='create_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
]