from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cclr_programs/', views.cclr_programs, name='cclr_programs'),
    path('dual_track_learning/', views.dual_track_learning,
         name='dual_track_learning'),
    path('hybrid_learning/', views.hybrid_learning, name='hybrid_learning'),
    path('online_diploma_program/', views.online_diploma_program,
         name='online_diploma_program'),
    path('programs/', views.programs,
         name='programs'),
    path('college_mentorship/', views.college_mentorship,
         name='college_mentorship'),
    path('highschool_mapping/', views.highschool_mapping,
         name='highschool_mapping'),
    path('faculty/', views.faculty,
         name='faculty'),

]
