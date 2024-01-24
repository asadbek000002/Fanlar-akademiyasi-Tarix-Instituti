from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)


class ConferencesCategory(BaseModel):
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Conferences Category'
        verbose_name_plural = 'Conferences Category'

    def __str__(self):
        return self.title


class Conferences(BaseModel):
    category = models.ForeignKey(ConferencesCategory, on_delete=models.CASCADE, related_name='category')
    title = models.CharField(max_length=250)
    context = models.TextField()

    class Meta:
        verbose_name = 'Conference'
        verbose_name_plural = 'Conferences'

    def __str__(self):
        return self.title


class ConferencesImg(BaseModel):
    conferences_img = models.ForeignKey(Conferences, on_delete=models.CASCADE, related_name='conferences_img')
    image = models.ImageField(blank=True, null=True)
