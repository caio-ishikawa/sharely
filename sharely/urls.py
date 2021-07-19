from django.contrib import admin
from django.urls import path,  include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('register/', include('main.urls')),
    path('login/', include('main.urls')),
    path('upload/', include('main.urls')),
    path('logout/', include('main.urls')),
    path('folder/<int:pk>/', include('main.urls')),
    path('folder/add/', include('main.urls')),
    #path('add/<int:pk>/<int:folder_id>/', include('main.urls')),
    path('add/<int:id>/<int:pk>/', include('main.urls')),
    path('add/user/<int:pk>/', include('main.urls')),
    path('search/', include('main.urls')),
    path('user/search/', include('main.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
