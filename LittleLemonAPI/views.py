from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import MenuItemSerializer
from .models import MenuItem

# Create your views here.
# The view uses BOTH the model and the serializer
class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "this is a protected view"})
