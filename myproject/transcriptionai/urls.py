from django.urls import path
from . import views

urlpatterns = [
    path('run_pipeline/', views.run_pipeline, name='run_pipeline'),
    path('realtime_transcription/', views.realtime_transcription_view, name='realtime_transcription'),

]
