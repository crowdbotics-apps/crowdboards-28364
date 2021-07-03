from home.models import Applications, Plans, Subscriptions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from home.api.v1.serializers import (
    ApplicationsSerializer,
    SignupSerializer,
    SubscriptionsSerializer,
    UserSerializer,
)


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


class ApplicationsViewSet(ModelViewSet):
    """
    A simple ViewSet for listing or retrieving all applications.
    """
    def list(self, request):
        queryset = Applications.objects.all()
        serializer = ApplicationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Applications.objects.all()
        apps = get_object_or_404(queryset, pk=pk)
        # TODO: change serializers of new code
        serializer = ApplicationsSerializer(apps)
        return Response(serializer.data)

class SubscriptionsViewSet(ModelViewSet):
    """
    A simple ViewSet for listing or retrieving subscription plans.
    """
    def list(self, request):
        queryset = Subscriptions.objects.all()
        serializer = SubscriptionsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Subscriptions.objects.all()
        subscriptions = get_object_or_404(queryset, pk=pk)
        serializer = SubscriptionsSerializer(subscriptions)
        return Response(serializer.data)

class PlansViewSet(ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = Plans.objects.all()
    serializer = UserSerializer(queryset, many=True)
    # serializer_class = AccountSerializer
