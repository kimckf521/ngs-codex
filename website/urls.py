from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Partner With Us
    path('cclr_programs/', views.cclr_programs, name='cclr_programs'),
    path('dual_track_learning/', views.dual_track_learning,
         name='dual_track_learning'),
    path('hybrid_learning/', views.hybrid_learning, name='hybrid_learning'),
    path('online_diploma_program/', views.online_diploma_program,
         name='online_diploma_program'),
    # Study With Us
    path('programs/', views.programs,
         name='programs'),
    path('college_mentorship/', views.college_mentorship,
         name='college_mentorship'),
    path('highschool_mapping/', views.highschool_mapping,
         name='highschool_mapping'),
    path('faculty/', views.faculty,
         name='faculty'),
    # Admissions
    path('admissions/', views.admissions,
         name='admissions'),
    # Join Ngs Commmunity
    path('ngs_inspires/', views.ngs_inspires,
         name='ngs_inspires'),
    path('ngs_connects/', views.ngs_connects,
         name='ngs_connects'),
    path('membership_signin/', views.membership_signin,
         name='membership_signin'),

    # CHINESE PAGES
    path('index_zh/', views.index_zh, name='index_zh'),

]
