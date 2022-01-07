from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include, static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('cms.urls')),
] + static.static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


admin.site.site_header = "Gobal Admin Site Panel"
admin.site.site_title = "Gobal Admin Site Portal"
admin.site.index_title = "Welcome to Gobal Admin Site Researcher Portal"