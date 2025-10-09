from django.shortcuts import render


def index(request):
    return render(request, 'website/index.html')


def privacy(request):
    return render(request, 'website/privacy_policy.html')


def terms(request):
    return render(request, 'website/terms_of_service.html')

# Partner With Us


def cclr_programs(request):
    return render(request, 'website/partner_with_us/cclr_programs.html')


def hybrid_learning(request):
    return render(request, 'website/partner_with_us/hybrid_learning.html')


def dual_track_learning(request):
    return render(request, 'website/partner_with_us/dual_track_learning.html')


def online_diploma_program(request):
    return render(request, 'website/partner_with_us/online_diploma_program.html')

# Study With Us


def programs(request):
    return render(request, 'website/study_with_us/programs.html')


def college_mentorship(request):
    return render(request, 'website/study_with_us/college_mentorship.html')


def highschool_mapping(request):
    return render(request, 'website/study_with_us/highschool_mapping.html')


def faculty(request):
    return render(request, 'website/study_with_us/faculty.html')


# Admissions

def admissions(request):
    return render(request, 'website/admissions/admissions.html')


# Join Ngs Commmunity

def ngs_inspires(request):
    return render(request, 'website/join_ngs_commmunity/ngs_inspires.html')


def ngs_connects(request):
    return render(request, 'website/join_ngs_commmunity/ngs_connects.html')


def membership_signin(request):
    return render(request, 'website/join_ngs_commmunity/membership_signin.html')

# CHINESE PAGES

# index.html


def index_zh(request):
    return render(request, 'website/language/zh/index_zh.html')


def privacy_zh(request):
    return render(request, 'website/language/zh/privacy_policy_zh.html')


def terms_zh(request):
    return render(request, 'website/language/zh/terms_of_service_zh.html')

# Partner With Us


def cclr_programs_zh(request):
    return render(request, 'website/language/zh/partner_with_us/cclr_programs_zh.html')


def hybrid_learning_zh(request):
    return render(request, 'website/language/zh/partner_with_us/hybrid_learning_zh.html')


def dual_track_learning_zh(request):
    return render(request, 'website/language/zh/partner_with_us/dual_track_learning_zh.html')


def online_diploma_program_zh(request):
    return render(request, 'website/language/zh/partner_with_us/online_diploma_program_zh.html')


# Study With Us

def programs_zh(request):
    return render(request, 'website/language/zh/study_with_us/programs_zh.html')


def college_mentorship_zh(request):
    return render(request, 'website/language/zh/study_with_us/college_mentorship_zh.html')


def highschool_mapping_zh(request):
    return render(request, 'website/language/zh/study_with_us/highschool_mapping_zh.html')


def faculty_zh(request):
    return render(request, 'website/language/zh/study_with_us/faculty_zh.html')


# Admissions

def admissions_zh(request):
    return render(request, 'website/language/zh/admissions/admissions_zh.html')


# Join Ngs Community

def ngs_inspires_zh(request):
    return render(request, 'website/language/zh/join_ngs_commmunity/ngs_inspires_zh.html')


def ngs_connects_zh(request):
    return render(request, 'website/language/zh/join_ngs_commmunity/ngs_connects_zh.html')


def membership_signin_zh(request):
    return render(request, 'website/language/zh/join_ngs_commmunity/membership_signin_zh.html')
