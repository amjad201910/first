from django.urls import path,include
from rest_framework import routers
from .views import advertiserCreat, advertisementViewsets

router = routers.DefaultRouter()
router.register(r'advertisement', advertisementViewsets, basename="advertisement")

urlpatterns = [
    path('', advertiserCreat.as_view(), name="advertiser-creat"),

    
    path('', include(router.urls)),

]