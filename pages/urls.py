from django.urls import path
from .views import HomePageView, AboutPageView

#create views and add imports above
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    
    
]