from django.urls import path
from api.views_api.department import CategoryListCreateView, DepartmentListCreateView, EmployeeListCreateView, ResearchListCreateView, WorksListCreateView

urlpatterns = [
    path('category/',CategoryListCreateView.as_view()),
    path('department/', DepartmentListCreateView.as_view()),
    path('employee/', EmployeeListCreateView.as_view()),
    path('research/', ResearchListCreateView.as_view()),
    path('work/', WorksListCreateView.as_view()),

]