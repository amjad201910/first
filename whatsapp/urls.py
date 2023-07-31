from django.urls import path,include
from rest_framework import routers
from .views import redirectTO ,chatSU
router = routers.DefaultRouter()
urlpatterns = [
   
    path('', include(router.urls)),
    path('redirectTO/<int:pk>/<str:uuid>', redirectTO.as_view(), name="redirectTO"),
    path('chat/', chatSU.as_view(), name="chat"),


]