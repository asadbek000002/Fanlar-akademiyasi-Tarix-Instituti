from django.urls import path
# department 
from api.views_api.department import  DepartmentListView, EmployeeListView, \
                        ResearchListView, PoemsListView, DepartmentDetailView
# library

from api.views_api.library import CategoryLibListView, SourceListView, ArchiveListView, \
                        RequirementListView, EditorialListView,\
                        AutoReferatListView, ElektronBookListView

# aboutinstitut
from api.views_api.aboutinstitut_view import LeadershipAPIView, OrganizationStructureAPIView, \
                        ArchitecturalLegalDocumentsAPIView, HistoryInstituteAPIView, NewsAPIView
# international_contact
from api.views_api.internetionalContact_view import PartnerOrganizationsAPIView, DoneInternationalProjectsAPIView, \
                        NotDoneInternationalProjectsAPIView, InternationalResearchersAPIView
# 9246692
urlpatterns = [

    # department
    path('department/', DepartmentListView.as_view()),
    path('dep/<id>/', DepartmentDetailView.as_view()),
    path('dep/<id>/employee/', EmployeeListView.as_view()),
    path('dep/<id>/research/', ResearchListView.as_view()),
    path('poems/', PoemsListView.as_view()),


    # library
    path('category_lib/',CategoryLibListView.as_view()),
    path('archive/', ArchiveListView.as_view()),
    path('requirements/', RequirementListView.as_view()),
    path('edorial/', EditorialListView.as_view()),
    path('elektron/', ElektronBookListView.as_view()),
    path('autoref/', AutoReferatListView.as_view()),
    path('source/', SourceListView.as_view()),
    
    # leadership
    path('leadership/', LeadershipAPIView.as_view()),
    path('organization-structure/', OrganizationStructureAPIView.as_view()),
    path('architectural-legal-documents/', ArchitecturalLegalDocumentsAPIView.as_view()),
    path('history-institute/', HistoryInstituteAPIView.as_view()),
    path('news/', NewsAPIView.as_view()),

    # international_contact
    path('partner-organizations/', PartnerOrganizationsAPIView.as_view()),
    path('done-international-projects/', DoneInternationalProjectsAPIView.as_view()),
    path('not-done-international-projects/', NotDoneInternationalProjectsAPIView.as_view()),
    path('international-researchers/', InternationalResearchersAPIView.as_view()),
]




