from django.urls import path
from . import views

urlpatterns = [
   path('',views.Category_List),
]