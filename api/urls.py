from django.urls import path
# department 
from api.views_api.department import CategoryListCreateView, DepartmentListCreateView, EmployeeListCreateView, \
                        ResearchListCreateView, WorksListCreateView
# library
from api.views_api.library import CategoryLibListCreateView, SourceListCreateView, ArchiveListCreateView, RequirementListCreateView, EditorialListCreateView, AutoReferatListCreateView, ElektronBookListCreateView 
from api.views_api.library import CategoryLibListCreateView, SourceListCreateView, ArchiveListCreateView, \
                        RequirementListCreateView, EditorialListCreateView, EditorialManyListCreateView, \
                        AutoReferatListCreateView, ElektronBookListCreateView
# aboutinstitut
from api.views_api.aboutinstitut_view import LeadershipAPIView, OrganizationStructureAPIView, \
                        ArchitecturalLegalDocumentsAPIView, HistoryInstituteAPIView, NewsAPIView
# internetionalContact
from api.views_api.internetionalContact_view import PartnerOrganizationsAPIView, DoneInternationalProjectsAPIView, \
                        NotDoneInternationalProjectsAPIView, InternationalResearchersAPIView

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
    
    # leadership
    path('leadership/', LeadershipAPIView.as_view()),
    path('organization-structure/', OrganizationStructureAPIView.as_view()),
    path('architectural-legal-documents/', ArchitecturalLegalDocumentsAPIView.as_view()),
    path('history-institute/', HistoryInstituteAPIView.as_view()),
    path('news/', NewsAPIView.as_view()),

    # internetionalContact
    path('partner-organizations/', PartnerOrganizationsAPIView.as_view()),
    path('done-international-projects/', DoneInternationalProjectsAPIView.as_view()),
    path('not-done-international-projects/', NotDoneInternationalProjectsAPIView.as_view()),
    path('international-researchers/', InternationalResearchersAPIView.as_view()),
]




