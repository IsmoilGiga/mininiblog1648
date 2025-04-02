from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import blog_detail, home_page, contact

urlpatterns = [
    path('', home_page, name='home'),
    path('blog/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('contact/', contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
