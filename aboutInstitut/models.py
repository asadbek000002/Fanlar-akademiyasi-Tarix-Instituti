from django.db import models

class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)
    

    class Meta:
        abstract = True
        ordering = ('id',)



class Department(BaseModel):
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
    departmentemp = models.ForeignKey(Department, on_delete=models.CASCADE, related_name= 'departmentemp')
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
        return self.title

class Works(BaseModel):
    employee = models.ForeignKey(Employee,  on_delete=models.CASCADE, related_name= 'employee')
    works = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'work'
        verbose_name_plural = 'work'
        abstract = False 
        ordering = ('id',)

    def __str__(self):
        return self.title
    
class Research(BaseModel):
    departmentres = models.ForeignKey(Department, on_delete=models.CASCADE, related_name= 'departmentres')
    context = models.TextField()
    

    class Meta:
        verbose_name = 'research'
        verbose_name_plural = 'researches'
        abstract = False  
        ordering = ('id',)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


