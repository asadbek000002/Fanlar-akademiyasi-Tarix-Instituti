from django.urls import path
from .views import CategoryListCreateView, DepartmentListCreateView, EmployeeListCreateView, ResearchListCreateView, WorkListCreateView

urlpatterns = [
    path('category/',CategoryListCreateView.as_view()),
    path('department/', DepartmentListCreateView.as_view()),
    path('employee/', EmployeeListCreateView.as_view()),
    path('research/', ResearchListCreateView.as_view()),
    path('work/', WorkListCreateView.as_view()),

]
