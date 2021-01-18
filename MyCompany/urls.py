from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('services/', include('services.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('pricing/', include('pricing.urls')),
    path('blog/', include('blogs.urls')),
    path('contact/', include('contacts.urls')),
    path('account/', include('accounts.urls')),
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
