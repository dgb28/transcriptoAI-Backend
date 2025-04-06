from django.urls import path
from . import views  # Correct import of views

urlpatterns = [
    path('run_pipeline/', views.run_pipeline, name='run_pipeline'),
]
