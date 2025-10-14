from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('privacy/', views.privacy, name='privacy'),
    path('termsofservice/', views.terms, name='terms'),
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
    path('', views.index_zh, name='index_zh'),
    path('privacy_zh/', views.privacy_zh, name='privacy_zh'),
    path('termsofservice_zh/', views.terms_zh, name='terms_zh'),
    # Partner With Us
    path('cclr_programs_zh/', views.cclr_programs_zh, name='cclr_programs_zh'),
    path('dual_track_learning_zh/', views.dual_track_learning_zh,
         name='dual_track_learning_zh'),
    path('hybrid_learning_zh/', views.hybrid_learning_zh,
         name='hybrid_learning_zh'),
    path('online_diploma_program_zh/', views.online_diploma_program_zh,
         name='online_diploma_program_zh'),

    # Study With Us
    path('programs_zh/', views.programs_zh,
         name='programs_zh'),
    path('college_mentorship_zh/', views.college_mentorship_zh,
         name='college_mentorship_zh'),
    path('highschool_mapping_zh/', views.highschool_mapping_zh,
         name='highschool_mapping_zh'),
    path('faculty_zh/', views.faculty_zh,
         name='faculty_zh'),

    # Admissions
    path('admissions_zh/', views.admissions_zh,
         name='admissions_zh'),

    # Join Ngs Community
    path('ngs_inspires_zh/', views.ngs_inspires_zh,
         name='ngs_inspires_zh'),
    path('ngs_connects_zh/', views.ngs_connects_zh,
         name='ngs_connects_zh'),
    path('membership_signin_zh/', views.membership_signin_zh,
         name='membership_signin_zh'),

    # Partner Form Submission (Email)
    path('partner_with_us/', views.partner_with_us, name='partner_with_us'),

]
