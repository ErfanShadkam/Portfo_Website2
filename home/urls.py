from django.urls import path
from home import views
from .views import submit_form
from Portfo_Website import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    path('submit-form/', submit_form, name='submit_form'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)