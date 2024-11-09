from django.urls import path
from .views import home, character_sheet_list, character_sheet_create
from . import views

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('charactersheets/', character_sheet_list, name='character_sheet_list'),
    path('charactersheets/create/', character_sheet_create, name='character_sheet_create'),
    path('sheet/<int:pk>/', views.character_sheet_detail, name='character_sheet_detail'),
    path('sheet/<int:pk>/update_health/', views.update_health, name='update_health'),
    path('sheet/<int:pk>/edit/', views.character_sheet_edit, name='character_sheet_edit'),
]
