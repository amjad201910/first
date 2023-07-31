from django.urls import path,include
from rest_framework import routers
from .views import complaintsCreate,opinionCreate

router = routers.DefaultRouter()
urlpatterns = [

    path('', include(router.urls)),
    path('complaint/', complaintsCreate.as_view(), name="complaints-Creat"),
    path('opinion/', opinionCreate.as_view(), name="opinion-Create"),

    


]