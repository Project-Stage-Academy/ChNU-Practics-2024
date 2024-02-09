from django.contrib.auth import authenticate
from django.contrib.auth import login
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer
from .serializers import UserLoginSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            # The serializer's validate method has been executed successfully
            user = authenticate(request, email=serializer.validated_data["email"], password=serializer.validated_data["password"])

            if user is not None:
                # Authenticate the user
                login(request, user)

                # You can customize the response as needed
                return Response({
                    "id": serializer.validated_data["id"],
                    "username": serializer.validated_data["username"],
                    "access_token": serializer.validated_data["access_token"]
                }, status=status.HTTP_200_OK)
            else:
                # Authentication failed
                return Response({"error": "Authentication failed"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # The serializer's validate method encountered validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
