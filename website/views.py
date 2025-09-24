from django.shortcuts import render


def index(request):
    return render(request, 'website/index.html')

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


# Join Ngs Commmunity
