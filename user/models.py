from django.db import models

# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=30)
 
    def __str__(self):
        return self.name

class Branch(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    age = models.IntegerField(default=0, editable=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='0')
    phone_number = models.CharField(max_length=15, blank=True)
    mail_id = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    college = models.ForeignKey(College, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name 