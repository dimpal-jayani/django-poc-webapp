from django.urls import path
from . import views

urlpatterns = [
    path('api/v1.0/snippet', views.SnippetList.as_view())
]