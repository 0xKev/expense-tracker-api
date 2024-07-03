from django.urls import path, include
from .views import *

from rest_framework import routers
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view


router = routers.DefaultRouter()
router.register(r'expense', ExpenseViewSet, basename="expense")


urlpatterns = [
    path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("sign-up/", SignUpView.as_view(), name="sign-up")
]