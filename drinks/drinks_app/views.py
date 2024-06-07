from .models import Drink
from rest_framework.authtoken.models import Token
from .models import CustomUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import DrinkSerializer, UserRegisterSerializer, TokenSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
import logging
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.views import LoginView, LogoutView
from django.contrib.auth import logout


logger = logging.getLogger(__name__)

# Create your views here.


@api_view(["GET", "POST"])
# @permission_classes([IsAuthenticated])
def drink_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 5
    if request.method == "GET":
        drinks = Drink.objects.all().order_by("-id")
        paginator_drinks = paginator.paginate_queryset(drinks, request)
        serializer = DrinkSerializer(paginator_drinks, many=True)
        return paginator.get_paginated_response(serializer.data)

    if request.method == "POST":
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Drink created successfully.")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning("Failed to create drink. Bad request.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
# @permission_classes([IsAuthenticated])
def drinks_details(request, pk):
    try:
        drink = Drink.objects.get(pk=pk)
    except:
        logger.warning(f"Drink with id {pk} not found.")
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Drink with id {pk} updated successfully.")
            return Response(serializer.data)
        logger.warning(f"Failed to update drink with id {pk}. Bad request.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        logger.warning(f"Failed to update drink with id {pk}. Bad request.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        drink.delete()
        logger.info(f"Drink with id {pk} deleted successfully.")
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegisterUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("User registered successfully.")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning("User registration failed: Bad request")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomLoginAPI(LoginView):
    """Custom Login API"""

    def get_response(self):
        serializer_class = TokenSerializer
        serializer = serializer_class(instance=self.token)
        logger.info("sucessfully logged in")
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomLogoutView(LogoutView):

    def post(self, request, format=None):
        # Deleting the authentication token associated with the user
        request.user.auth_token.delete()

        # Logging the user logout
        logger.info(f"User {request.user} logged out successfully.")

        # Logging out the user from the session
        logout(request)

        # Creating a response for the successful logout
        response = Response(
            {"detail": ("Successfully logged out.")},
            status=status.HTTP_200_OK,
        )
        return response
