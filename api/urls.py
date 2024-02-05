from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import path

# department 
from api.views_api.department import DepartmentListView, EmployeeListView, \
    ResearchListView, PoemsListView, DepartmentDetailView

# library

from api.views_api.library import CategoryLibListView, SourceListView, ArchiveListView, \
    RequirementListView, EditorialListView, \
    AutoReferatListView, ElektronBookListView

# aboutinstitut
from api.views_api.aboutinstitut_view import LeadershipAPIView, OrganizationStructureAPIView, \
    ArchitecturalLegalDocumentsAPIView, HistoryInstituteAPIView, NewsAPIView
# international_contact
from api.views_api.internetionalContact_view import PartnerOrganizationsAPIView, DoneInternationalProjectsAPIView, \
    NotDoneInternationalProjectsAPIView, InternationalResearchersAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # richtextfield
    path('djrichtextfield/', include('djrichtextfield.urls')),

    # department
    path('department/', DepartmentListView.as_view()),
    path('dep/<id>/', DepartmentDetailView.as_view()),
    path('dep/<id>/employee/', EmployeeListView.as_view()),
    path('dep/<id>/research/', ResearchListView.as_view()),
    path('poems/', PoemsListView.as_view()),

    # library
    path('category_lib/', CategoryLibListView.as_view()),
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
