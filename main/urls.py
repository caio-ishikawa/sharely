from django.urls import path,  include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('upload/', views.uploadView, name='upload'),
    path('logout/', views.logoutView, name='logout'),
    path('folder/<int:pk>/', views.folderView, name='folder'),
    path('folder/add/', views.createFolder, name='folder'),
    #path('add/<int:pk>/<int:folder_id>/', views.addFile, name='add_file')
    path('add/<int:pk>/<str:id>/', views.addFile, name='add_file'),
]
