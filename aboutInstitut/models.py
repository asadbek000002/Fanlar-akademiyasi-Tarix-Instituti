<<<<<<< HEAD
from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True
        ordering = ('id',)


# RAHBARIYAT
class Leadership(BaseModel):
    position = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    phone_number = models.IntegerField(max_length=13)
    email = models.EmailField()
    reception_days = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/aboutInstitut/leadership')

    class Meta:
        verbose_name = 'Leadership'
        verbose_name_plural = 'Leaderships'
        abstract = False
        ordering = ('id',)

    def __str__(self):
        return self.full_name


class LeadershipImage(BaseModel):
    leadership_img = models.ForeignKey(Leadership, on_delete=models.CASCADE,
                                       related_name='leadership_img')
    image = models.ImageField(blank=True, null=True)


# TASHKILIY TUZILMA
class OrganizationStructure(BaseModel):
    image = models.ImageField(upload_to='images/aboutInstitut/organization_structure')

    class Meta:
        verbose_name = 'Organization Structure'
        verbose_name_plural = 'Organization Structures'
        abstract = False
        ordering = ('id',)

    def __str__(self):
        return self.image


class OrganizationStructureImage(BaseModel):
    organization_structure_img = models.ForeignKey(OrganizationStructure, on_delete=models.CASCADE,
                                                   related_name='organization_structure_img')
    image = models.ImageField(blank=True, null=True)


# MEMORIY-HUQUQIY HUJJATLAR
class ArchitecturalLegalDocuments(BaseModel):
    title = models.CharField(max_length=250)
    context = models.TextField()

    class Meta:
        verbose_name = 'Architectural Legal Document'
        verbose_name_plural = 'Architectural Legal Documents'
        abstract = False
        ordering = ('id',)

    def __str__(self):
        return self.title


# INSTITUT TARIXI
class HistoryInstitute(BaseModel):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/aboutInstitut/history_institute')
    contex = models.TextField()

    class Meta:
        verbose_name = 'History Institute'
        verbose_name_plural = 'History Institutes'
        abstract = False
        ordering = ('id',)

    def __str__(self):
        return self.title


class HistoryInstituteImage(BaseModel):
    history_institute_img = models.ForeignKey(HistoryInstitute, on_delete=models.CASCADE,
                                              related_name='history_institute_img')
    image = models.ImageField(blank=True, null=True)


# YANGILIKLAR
class News(BaseModel):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/aboutInstitut/news')
    context = models.TextField()


class NewsImage(BaseModel):
    news_img = models.ForeignKey(News, on_delete=models.CASCADE,
                                 related_name='news_img')
    image = models.ImageField(blank=True, null=True)
=======
>>>>>>> origin/main
