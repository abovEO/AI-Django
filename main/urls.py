from django.contrib import admin
from django.urls import path,include
from main import views

urlpatterns = [
    
    #path('admin/', admin.site.urls),
    path('',views.index, name='main'),
    path('login',views.login, name='login'),
    path("map/",views.map, name='map'),
    
    path("devices/",views.devices, name='devices'),
    path("camerastreaming/",views.camerastreaming, name='camerastreaming'),
    path("cameramanagement/",views.cameramanagement, name='cameramanagement'),

    path('mask_feed', views.mask_feed, name='mask_feed'),
    path('livecam_feed', views.livecam_feed, name='livecam_feed'),


    path('pageInput/', views.pageInput, name="pageInput"),

    path("videoss/",views.videoss, name='map'),
    
    path('captureinput/', views.datasetin, name="capturedata"),
    

    
]