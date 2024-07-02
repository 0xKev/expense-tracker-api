from django.urls import path, include
from .views import *

from rest_framework import routers
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view


router = routers.DefaultRouter()
router.register(r'expense', ExpenseViewSet, basename="expense")

# added just to have api view of both cbv and fbv
@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "expenses": reverse("expense-list", request=request, format=format),
        "sign-up": reverse("sign-up", request=request, format=format)
    })


urlpatterns = [
    path("", api_root, name="api-root"),
    path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("sign-up/", SignUpView.as_view(), name="sign-up")
]