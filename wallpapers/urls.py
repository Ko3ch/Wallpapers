from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='wallpapers-home'),
    path('search/', views.search_results, name='wallpapers-search'),
    path('image/<int:id>', views.image_by_id, name='wallpapers-single_image'),
    path('location/<int:id>', views.images_by_location, name='wallpapers-image_location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)