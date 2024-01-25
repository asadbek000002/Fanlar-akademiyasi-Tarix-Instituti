from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True
        ordering = ('id',)


class Category(BaseModel):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Category_lib'
        verbose_name_plural = 'Categories_lib'

    def __str__(self):
        return self.title

# Arxiv
class Archive(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/library/archive')
    category_arch = models.ForeignKey(Category, on_delete= models.CASCADE, related_name = 'category_arch')


    class Meta:
        verbose_name = 'Archive'
        verbose_name_plural = 'Archives'

    def __str__(self):
        return self.title

# Talablar
class Requirement(BaseModel):
    title = models.CharField(max_length=255)
    context = models.TextField()
    image = models.ImageField(upload_to='images/library/requirements/')
    category_req = models.ForeignKey(Category, on_delete= models.CASCADE, related_name = 'category_req')



    class Meta:
        verbose_name = 'Requirement'
        verbose_name_plural = 'Requirements'

    def __str__(self):
        return self.title
# Tahririyat
class Editorial(BaseModel):
    fullname = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    ish_joyi = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/library/editorial/')
    category_edit = models.ForeignKey(Category, on_delete= models.CASCADE, related_name = 'category_edit')



    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editorials'

    def __str__(self):
        return self.fullname

# Tahririyat Kop fieldli
class EditorialMany(BaseModel):
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name = 'editorial')
    fullname = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    ish_joyi = models.CharField(max_length=255, blank=True, null=True)


# Elektron kitoblar
class ElectronBook(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/library/elektron_book/')


    class Meta:
        verbose_name = 'Elektronbook'
        verbose_name_plural = 'Elektronbooks'

    def __str__(self):
        return self.title

# AvtoReferat
class AutoReferat(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/library/autoreferat/')


    class Meta:
        verbose_name = 'Autoreferat'
        verbose_name_plural = 'Autoreferats'

    def __str__(self):
        return self.title

# Manbalar
class Source(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/library/source/')


    class Meta:
        verbose_name = 'Source'
        verbose_name_plural = 'Sources'

    def __str__(self):
        return self.title
