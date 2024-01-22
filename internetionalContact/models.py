from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)


class PartnerOrganizations(BaseModel):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/internetionalContact/partner_organizations')
    context = models.TextField()


# XALQARO LOYHALAR
class InternationalProjects(BaseModel):
    PROJECT_STATUS = (
        ('bajarilgan', 'Bajarilgan'),
        ('bajarilmagan', 'Bajarilmagan'),
    )

    project_name = models.CharField(max_length=250)
    partner_organization = models.CharField(max_length=250)
    funding_organization = models.CharField(max_length=250)
    done_undone_year = models.IntegerField()
    project_status = models.CharField(max_length=20, choices=PROJECT_STATUS, default='bajarilmagan')
    image = models.ImageField(upload_to='images/internetionalContact/international_projects')

    class Meta:
        verbose_name = 'International Project'
        verbose_name_plural = 'International Projects'

    def __str__(self):
        return self.project_name


class InternationalResearchers(BaseModel):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/internetionalContact/international_researchers')


class InternationalResearchersExpert(BaseModel):
    researchers = models.ForeignKey(InternationalResearchers, on_delete=models.CASCADE,
                                                        related_name='researchers')
    full_name = models.CharField(max_length=250)
    activity_institution = models.CharField(max_length=350)
    year_of_visit = models.IntegerField()
