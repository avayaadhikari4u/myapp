
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "E-com Admin pannel"
admin.site.site_title = "E-Com Staff"
admin.site.index_title = "Welcome to E-com Nepal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('store.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
