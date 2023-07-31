from django.urls import path,include
from rest_framework import routers
from .views import opinionViewsets ,complaintsViewsets,country

router = routers.DefaultRouter()
router.register(r'opinions', opinionViewsets, basename="opinion")
router.register(r'complaints', complaintsViewsets, basename="complaints")

urlpatterns = [

    path('', include(router.urls)),
    path('country/', country.as_view(), name="country"),




]