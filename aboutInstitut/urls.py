from django.urls import path
from .views import LeadershipApiList

urlpatterns = [
    path('your-model-list/', LeadershipApiList.as_view(), name='your-model-list'),
]
