from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, permissions, viewsets
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer


def home(request):
    return render(request, "home.html", {})


class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected."})
