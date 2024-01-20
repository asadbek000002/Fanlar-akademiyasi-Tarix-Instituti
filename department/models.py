from django.db import models
from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True
        ordering = ('id',)


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Department(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_dep')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/department/depart')
    context = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'department'
        verbose_name_plural = 'departments'
        abstract = False
        ordering = ('id',)


class Employee(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_emp')
    departmentemp = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_emp')
    fullname = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    email = models.EmailField()
    bio = models.TextField()
    image = models.ImageField(upload_to='images/department/employee/')

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'

    def __str__(self):
        return self.fullname


class Works(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_work')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee')
    works = models.TextField()

    class Meta:
        verbose_name = 'work'
        verbose_name_plural = 'works'
        abstract = False
        ordering = ('id',)

    def __str__(self):
        return self.works


class Research(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_res')
    departmentres = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_res')
    context = models.TextField()

    class Meta:
        verbose_name = 'research'
        verbose_name_plural = 'researches'
        abstract = False
        ordering = ('id',)

    def __str__(self):
        return self.context
