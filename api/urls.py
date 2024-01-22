from django.urls import path
# department 
from api.views_api.department import CategoryListCreateView, DepartmentListCreateView, EmployeeListCreateView, ResearchListCreateView, WorksListCreateView
# library
from api.views_api.library import CategoryLibListCreateView, SourceListCreateView, ArchiveListCreateView, RequirementListCreateView, EditorialListCreateView, EditorialManyListCreateView, AutoReferatListCreateView, ElektronBookListCreateView 

urlpatterns = [

    # department
    path('category_dep/',CategoryListCreateView.as_view()),
    path('department/', DepartmentListCreateView.as_view()),
    path('employee/', EmployeeListCreateView.as_view()),
    path('research/', ResearchListCreateView.as_view()),
    path('work/', WorksListCreateView.as_view()),


    # library
    path('category_lib/',CategoryLibListCreateView.as_view()),
    path('archive/', ArchiveListCreateView.as_view()),
    path('requirements/', RequirementListCreateView.as_view()),
    path('edorial/', EditorialListCreateView.as_view()),
    path('elektron/', ElektronBookListCreateView.as_view()),
    path('autoref/', AutoReferatListCreateView.as_view()),
    path('source/', SourceListCreateView.as_view()),
]