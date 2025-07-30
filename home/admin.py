from django.contrib import admin
from .models import Profile, Experience, ExperienceDetail,Contact, Job, SkillBox, Skill, Education, Certification , Portfolio ,PortfolioCategory


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
admin.site.register(PortfolioCategory)
@admin.register(Contact)
class contact_admin(admin.ModelAdmin):
    list_display = ('id','name','email','phone_number','short_comments','status')
    list_editable = ['status']
    List_per_page = 10
    search_fields = ['name','id']

    def short_comments(self, obj):
        return f'{obj.comments[:20]}...'  # Truncate the first 20 characters of the comments

    short_comments.short_description = 'Comments'