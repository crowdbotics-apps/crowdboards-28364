from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import (
    ApplicationsViewSet,
    PlansViewSet,
    SignupViewSet,
    LoginViewSet,
    SubscriptionsViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("app", ApplicationsViewSet, basename="apps")
router.register("subscriptions", SubscriptionsViewSet, basename="subscriptions")
router.register("plans", PlansViewSet, basename="plans")



urlpatterns = [
    path("", include(router.urls)),
]
