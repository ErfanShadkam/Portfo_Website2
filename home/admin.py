from django.contrib import admin
from .models import Profile, Experience, ExperienceDetail, Job, SkillBox, Skill, Education, Certification , Portfolio


# ----------- Job Admin -----------
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


# ----------- Profile Admin -----------
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'experience_level')
    search_fields = ('name', 'email', 'location')
    filter_horizontal = ('jobs',)


# ----------- Skill & SkillBox Admin -----------
class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ('name', 'percent', 'description')


@admin.register(SkillBox)
class SkillBoxAdmin(admin.ModelAdmin):
    inlines = [SkillInline]
    list_display = ('title',)
    search_fields = ('title',)


# ----------- Experience & ExperienceDetail Admin -----------
class ExperienceDetailInline(admin.TabularInline):
    model = ExperienceDetail
    extra = 1


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    inlines = [ExperienceDetailInline]
    list_display = ('title', 'company', 'start_at', 'end_at', 'is_current')
    search_fields = ('title', 'company')
    list_filter = ('is_current', 'start_at', 'end_at')

admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Portfolio)