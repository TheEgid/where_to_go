from django.contrib import admin
from django.urls import path, reverse
from django.conf import settings
from django.conf.urls.static import static
from places import views

urlpatterns = \
    [
        path('admin/', admin.site.urls),
        path('', views.show_main),
        path('places/<int:id>/', views.show_place, name='show_place'),

    ] \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
