from django.db import models


class Customer(models.Model):
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE,verbose_name='User')
  tc = models.CharField(verbose_name='Tc no',max_length=11, unique=True)
  name = models.CharField(max_length=50, verbose_name='Name')
  surname = models.CharField(max_length=50, verbose_name='Surname')
  phone = models.CharField(verbose_name='Tel no', max_length=11)
  city = models.CharField(max_length=50, verbose_name='Country')
  district = models.CharField(max_length=50, verbose_name='district')
  created_date = models.DateTimeField(auto_now_add=True, verbose_name='created date')

  def __str__(self):
    return self.name