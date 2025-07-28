from django.shortcuts import render
from .models import Profile , Job,SkillBox,Skill,Experience,Education,Certification

# Create your views here

def home(request):
    profile = Profile.objects.prefetch_related('jobs').first()
    skillboxes = SkillBox.objects.prefetch_related('skills').all()
    experiences = Experience.objects.filter(profile=profile)
    educations = profile.Educations.all()
    certifications = profile.Certifications.all()
    return render(request, 'home/index.html', {
        'profile': profile,
        'skillboxes': skillboxes,
        'experiences': experiences,
        'educations': educations,
        'certifications': certifications,  
    })
