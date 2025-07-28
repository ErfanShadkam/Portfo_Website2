from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Profile(models.Model):
    EXPERIENCE_LEVEL_CHOICES = [
        ('intern', 'Intern'),
        ('junior', 'Junior Developer'),
        ('mid', 'Mid-Level Developer'),
        ('senior', 'Senior Developer'),
        ('lead', 'Tech Lead'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    jobs = models.ManyToManyField(Job, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    email = models.EmailField(blank=True)
    instagram_link = models.URLField(blank=True)
    telegram_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    about_profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    about_title = models.CharField(max_length=100, blank=True)
    about_text = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    experience_level = models.CharField(
        max_length=10,
        choices=EXPERIENCE_LEVEL_CHOICES,
        default='junior',
        verbose_name='Experience Level'
    )
    about_Specialization = models.CharField(max_length=100, blank=True)
    about_Education = models.CharField(max_length=100, blank=True)
    about_Languages = models.CharField(max_length=100, blank=True)
    resume_link = models.URLField(blank=True)
    resume_professional_summary = models.TextField(blank=True)

    def __str__(self):
        return self.name


class SkillBox(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Skill(models.Model):
    skill_box = models.ForeignKey(SkillBox, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    percent = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.percent}%)"


class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences')
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255, default='Developer...')
    description = models.TextField()
    start_at = models.DateField()
    end_at = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} at {self.company}"


class ExperienceDetail(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='details')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='Educations')
    university = models.CharField(max_length=255)
    title = models.CharField(max_length=255, default='Developer...')
    description = models.TextField()
    start_at = models.DateField()
    end_at = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} at {self.university}"
    
    
class Certification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='Certifications')
    title = models.CharField(max_length=255)
    start_at = models.DateField()
    
    def __str__(self):
        return f"{self.title} "
    
class Portfolio(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='portfolios')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    github_link = models.URLField(blank=True)
    preview_link = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="resume_assets/img")
    
    def __str__(self):
        return f"{self.title}"