from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_protect
import os
import resend
from .forms import ContactForm
from .models import Profile, Job, SkillBox, Skill, Experience, Education, Certification, Contact, PortfolioCategory, Portfolio

resend.api_key = os.environ.get('RESEND_API_KEY')

# Create your views here

def home(request):
    profile = Profile.objects.prefetch_related('jobs').first()
    skillboxes = SkillBox.objects.prefetch_related('skills').all()
    experiences = Experience.objects.filter(profile=profile)
    educations = profile.Educations.all()
    certifications = profile.Certifications.all()

    portfolio_cat = PortfolioCategory.objects.prefetch_related('portfolios').all()
    portfolios = Portfolio.objects.select_related('category').all()

    return render(request, 'home/index.html', {
        'profile': profile,
        'skillboxes': skillboxes,
        'experiences': experiences,
        'educations': educations,
        'certifications': certifications,
        'portfolio_cat': portfolio_cat,
        'portfolios': portfolios,
    })


@csrf_protect
def submit_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                email_sender(data)
                contact_us(data)
                return JsonResponse({'success': True})
            except Exception as e:
                print(f"Error while sending email or saving to DB: {e}")
                return JsonResponse({'success': False, 'errors': {'form': [str(e)]}}, status=400)
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    return JsonResponse({'success': False, 'errors': {'form': ['Invalid request']}}, status=400)


def email_sender(data):
    subject = 'You have a contact'
    body = (
        f"Name: {data['name']}\n"
        f"Subject: {data['subject']}\n"
        f"Phone Number: {data['phone']}\n"
        f"Email: {data['email']}\n"
        f"Comments: {data['comments']}"
    )

    params = {
        "from": "onboarding@resend.dev",  # switch to your verified domain sender later, e.g. sender@erfanshadkam.ir
        "to": ["erfanshadkam@outlook.com"],
        "subject": subject,
        "text": body,
    }

    resend.Emails.send(params)


def contact_us(data):
    Contact.objects.create(
        name=data['name'],
        subject=data['subject'],
        phone_number=data['phone'],
        email=data['email'],
        comments=data['comments']
    )