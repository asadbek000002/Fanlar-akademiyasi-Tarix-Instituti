# from django.db import models
#
#
# class BaseModel(models.Model):
#     created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)
#
#
# class Communication(BaseModel):
#     address = models.CharField(max_length=250)
#     phone_number = models.CharField(max_length=13)
#     fax = models.CharField(max_length=20)
#     email = models.EmailField()
#
#     class Meta:
#         verbose_name = 'Communication'
#         verbose_name_plural = 'Communications'
#
#     def __str__(self):
#         return self.address
