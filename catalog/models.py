from django.db import models
from django.urls import reverse 
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator


class LocalPlane(models.Model):
    name = models.CharField(max_length=200, help_text="Enter Name of plane(eg. YH12)")
    description = models.TextField(max_length=1000, help_text="Enter a brief description")
    size_choice = (
        ('2','2'),
        ('4','4'),
        ('6','6'),
    )
    terminal = models.IntegerField(unique=True, validators=[
            MaxValueValidator(15),
            MinValueValidator(1)
    ])
    size = models.CharField(max_length=6, choices=size_choice, default='2')
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    def __str__(self):
        return self.name + ".........................................Terminal : " + str(self.terminal) + ".........................................DATE&TIME : " + str(self.date)
    def get_absolute_url(self):
        return reverse('apronone-detail', args=[str(self.id)])
    class Meta:
        unique_together = (("terminal","id"))
    
class InternationalPlane(models.Model):
    name = models.CharField(max_length=200, help_text="Enter Name of plane(eg. YH12)")
    description = models.TextField(max_length=1000, help_text="Enter a brief description")
    size_choice = (
        ('2','2'),
        ('4','4'),
        ('6','6'),
    )
    terminal = models.IntegerField(unique=True, validators=[
            MaxValueValidator(15),
            MinValueValidator(1)
    ])
    size = models.CharField(max_length=6, choices=size_choice, default='2')
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    def __str__(self):
        return self.name + ".........................................Terminal : " + str(self.terminal) + ".........................................DATE&TIME : " + str(self.date)
    def get_absolute_url(self):
        return reverse('aprontwo-detail', args=[str(self.id)])
    class Meta:
        unique_together = (("terminal","id"))

class CargoPlane(models.Model):
    name = models.CharField(max_length=200, help_text="Enter Name of plane(eg. YH12)")
    description = models.TextField(max_length=1000, help_text="Enter a brief description")
    size_choice = (
        ('2','2'),
        ('4','4'),
        ('6','6'),
    )
    terminal = models.IntegerField(unique=True, validators=[
            MaxValueValidator(15),
            MinValueValidator(1)
    ])
    size = models.CharField(max_length=6, choices=size_choice, default='2')
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    def __str__(self):
        return self.name + ".........................................Terminal : " + str(self.terminal) + ".........................................DATE&TIME : " + str(self.date)
    def get_absolute_url(self):
        return reverse('apronthree-detail', args=[str(self.id)])
    class Meta:
        unique_together = (("terminal","id"))

class Emergency(models.Model):
    name = models.CharField(max_length=200, help_text="Enter Name of plane(eg. YH12)")
    description = models.TextField(max_length=1000, help_text="Enter a brief description")
    size_choice = (
        ('2','2'),
        ('4','4'),
        ('6','6'),
    )
    size = models.CharField(max_length=6, choices=size_choice, default='2')
    plane_choice = (
        ('Domestic','Domestic'),
        ('International','International'),
        ('Cargo','Cargo'),
    )
    plane_type = models.CharField(max_length=15, choices=plane_choice, default='Domestic')
    terminal = models.IntegerField(unique=True, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
    ])
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    def __str__(self):
        return self.name + ".........................................Terminal : " + str(self.terminal) + ".........................................DATE&TIME : " + str(self.date)
    def get_absolute_url(self):
        return reverse('emergency-detail', args=[str(self.id)])
    class Meta:
        unique_together = (("terminal","id"))