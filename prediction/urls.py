from . import views
from django.urls import include, path

urlpatterns = [
    
    path('',views.homepage,name='homepage'),
    path('predict',views.predictpage,name='predictpage'),
    path('verify',views.verify,name='verify'),
    
    path('about',views.about,name='about'),
    path('services',views.service,name='services'),
    # path('pahanidetails',views.pahanidetails,name='pahanidetails'),
    path('prediction',views.prediction,name='prediction'),
]