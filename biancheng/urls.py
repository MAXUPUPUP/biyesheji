from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
urlpatterns = [
    path("admin/", admin.site.urls),
    path('user/', include('user.urls')),  # student
    path('lesson/', include('lesson.urls')),  # teacher
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
