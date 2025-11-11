from django.urls import path
from . import views

urlpatterns = [
    path('index_en', views.index_en, name='index_en'),
    path('privacy_en', views.privacy_en, name='privacy_en'),
    path('termsofservice_en', views.terms_en, name='terms_en'),
    # Partner With Us
    path('cclr_programs_en', views.cclr_programs_en, name='cclr_programs_en'),
    path('dual_track_learning_en', views.dual_track_learning_en,
         name='dual_track_learning_en'),
    path('hybrid_learning_en', views.hybrid_learning_en, name='hybrid_learning_en'),
    path('online_diploma_program_en', views.online_diploma_program_en,
         name='online_diploma_program_en'),
    # Study With Us
    path('programs_en', views.programs_en,
         name='programs_en'),
    path('college_mentorship_en', views.college_mentorship_en,
         name='college_mentorship_en'),
    path('highschool_mapping_en', views.highschool_mapping_en,
         name='highschool_mapping_en'),
    path('faculty_en', views.faculty_en,
         name='faculty_en'),
    # Admissions
    path('admissions_en', views.admissions_en,
         name='admissions_en'),
    # Join Ngs Commmunity
    path('ngs_inspires_en', views.ngs_inspires_en,
         name='ngs_inspires_en'),
    path('ngs_connects_en', views.ngs_connects_en,
         name='ngs_connects_en'),

    # In Progress
    path('in_progress_en', views.in_progress_en,
         name='in_progress_en'),

    # Tetsing
    path('test/', views.test, name='test'),

    # Partners
    path('yinghua_online_en', views.YCSOnline_en, name='yinghua_online_en'),
    path('ib_heros_en', views.ib_heros_en, name='ib_heros_en'),

    # CHINESE PAGES
    path('', views.index_zh, name='index_zh'),
    path('privacy', views.privacy_zh, name='privacy_zh'),
    path('termsofservice', views.terms_zh, name='terms_zh'),
    # Partner With Us
    path('cclr_programs', views.cclr_programs_zh, name='cclr_programs_zh'),
    path('dual_track_learning', views.dual_track_learning_zh,
         name='dual_track_learning_zh'),
    path('hybrid_learning', views.hybrid_learning_zh,
         name='hybrid_learning_zh'),
    path('online_diploma_program', views.online_diploma_program_zh,
         name='online_diploma_program_zh'),

    # Study With Us
    path('programs', views.programs_zh,
         name='programs_zh'),
    path('college_mentorship', views.college_mentorship_zh,
         name='college_mentorship_zh'),
    path('highschool_mapping', views.highschool_mapping_zh,
         name='highschool_mapping_zh'),
    path('faculty', views.faculty_zh,
         name='faculty_zh'),

    # Admissions
    path('admissions', views.admissions_zh,
         name='admissions_zh'),

    # Join Ngs Community
    path('ngs_inspires', views.ngs_inspires_zh,
         name='ngs_inspires_zh'),
    path('ngs_connects', views.ngs_connects_zh,
         name='ngs_connects_zh'),

    # In Progress
    path('in_progress', views.in_progress_zh,
         name='in_progress_zh'),

    # Partner Form Submission (Email)
    path('partner_with_us', views.partner_with_us, name='partner_with_us'),

    # Partners
    path('yinghua_online', views.YCSOnline_zh, name='yinghua_online_zh'),
    path('ib_heros', views.ib_heros_zh, name='ib_heros_zh'),

]
