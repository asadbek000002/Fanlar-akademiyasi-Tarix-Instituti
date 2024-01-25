from django.db import models
from djrichtextfield.models import RichTextField


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)


# RAHBARIYAT
class Leadership(BaseModel):
    position = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField()
    reception_days = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/about_institute/leadership')

    class Meta:
        verbose_name = 'Leadership'
        verbose_name_plural = 'Leaderships'

    def __str__(self):
        return self.full_name


class LeadershipImage(BaseModel):
    leadership_img = models.ForeignKey(Leadership, on_delete=models.CASCADE,
                                       related_name='leadership_img')
    image = models.ImageField(blank=True, null=True)


# TASHKILIY TUZILMA
class OrganizationStructure(BaseModel):
    image = models.ImageField(upload_to='images/about_institute/organization_structure')

    class Meta:
        verbose_name = 'Organization Structure'
        verbose_name_plural = 'Organization Structures'

    def __str__(self):
        return self.image.url


class OrganizationStructureImage(BaseModel):
    organization_structure_img = models.ForeignKey(OrganizationStructure, on_delete=models.CASCADE,
                                                   related_name='organization_structure_img')
    image = models.ImageField(blank=True, null=True)


# MEMORIY-HUQUQIY HUJJATLAR
class ArchitecturalLegalDocuments(BaseModel):
    title = models.CharField(max_length=250)
    context = RichTextField()

    class Meta:
        verbose_name = 'Architectural Legal Document'
        verbose_name_plural = 'Architectural Legal Documents'

    def __str__(self):
        return self.title


# INSTITUT TARIXI
class HistoryInstitute(BaseModel):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/about_institute/history_institute')
    contex = RichTextField()

    class Meta:
        verbose_name = 'History Institute'
        verbose_name_plural = 'History Institutes'

    def __str__(self):
        return self.title


class HistoryInstituteImage(BaseModel):
    history_institute_img = models.ForeignKey(HistoryInstitute, on_delete=models.CASCADE,
                                              related_name='history_institute_img')
    image = models.ImageField(blank=True, null=True)


# YANGILIKLAR
class News(BaseModel):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/about_institute/news')
    context = RichTextField()

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class NewsImage(BaseModel):
    news_img = models.ForeignKey(News, on_delete=models.CASCADE,
                                 related_name='news_img')
    image = models.ImageField(blank=True, null=True)
