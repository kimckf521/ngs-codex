from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import PartnerForm
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


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

# In Progress


def in_progress(request):
    return render(request, 'website/in_progress.html')


# Partners
def YCSOnline(request):
    return render(request, 'website/partners_lists/ycs/YCSOnline.html')


def ib_heros(request):
    return render(request, 'website/partners_lists/ib_heros/ib_heros.html')


# Testing


def test(request):
    return render(request, 'website/test.html')


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


# In Progress

def in_progress_zh(request):
    return render(request, 'website/language/zh/in_progress_zh.html')

# Partners


def YCSOnline_zh(request):
    return render(request, 'website/language/zh/partners_lists/ycs/YCSOnline_zh.html')


def ib_heros_zh(request):
    return render(request, 'website/language/zh/partners_lists/ib_heros/ib_heros_zh.html')

# Email views


@csrf_protect
def partner_with_us(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)

        # ✅ Validate the form before using cleaned_data
        if form.is_valid():
            name = form.cleaned_data['name']
            school_name = form.cleaned_data['school_name']
            email = form.cleaned_data['email']
            mobile_or_wechat = form.cleaned_data.get('mobile_or_wechat', '')
            help_description = form.cleaned_data['help_description']

            subject = f"New Partner Request from {name}"
            message = (
                f"Name: {name}\n"
                f"School: {school_name}\n"
                f"Email: {email}\n"
                f"Mobile/WeChat: {mobile_or_wechat}\n\n"
                f"How can we help:\n{help_description}"
            )

            try:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,     # from
                    [settings.EMAIL_RECEIVER],   # to (your inbox)
                    fail_silently=False,
                )

                messages.success(
                    request, 'Thanks! We will contact you shortly.')
                return redirect('index')
            except Exception as e:
                print(f"error {e}")
                messages.error(request, f"Unable to send message: {e}")

        else:
            # Form not valid → redisplay with errors
            messages.error(request, 'Please correct the errors below.')

    else:
        form = PartnerForm()

    return render(request, 'website/index.html', {'form': form})
