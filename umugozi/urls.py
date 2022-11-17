import imp 
from xml.dom.minidom import Document
from django.urls import path
from .import views
from .views import *

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.index, name='welcome'),
    path('signup/',views.register, name='signup'),
    path('signin/',views.login, name='signin')
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)