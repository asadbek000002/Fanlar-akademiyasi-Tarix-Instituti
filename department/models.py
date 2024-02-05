from django.db import models
# from djrichtextfield.models import RichTextField
from ckeditor.fields import RichTextField


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True
        ordering = ('id',)


class Department(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/department/Info/')
    context = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class Employee(BaseModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_employee')
    fullname = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    email = models.EmailField()
    bio = RichTextField()
    file = models.FileField()
    image = models.ImageField(upload_to='images/department/employee/')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.fullname


class Poems(BaseModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_poems')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee')
    works = RichTextField()

    class Meta:
        verbose_name = 'Poem'
        verbose_name_plural = 'Poems'

    def __str__(self):
        return self.works


class Research(BaseModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_research')
    context = RichTextField()

    class Meta:
        verbose_name = 'Research'
        verbose_name_plural = 'Researches'

    def __str__(self):
        return self.context
