from django.shortcuts import render
from .models import Leadership
from .serializers import LeadershipSerializer
from rest_framework.generics import ListAPIView


class LeadershipApiList(ListAPIView):
    queryset = Leadership.objects.all()
    serializer_class = LeadershipSerializer
