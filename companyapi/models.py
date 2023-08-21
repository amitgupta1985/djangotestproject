from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=50, choices=(
        ('IT', 'IT'),
        ('Non IT', 'Non IT'),
        ('Mobile Phone', 'Mobile Phone')
    ))
    added = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    about_me = models.TextField()
    position = models.CharField(max_length=50, choices=(
        ('TL', 'TL'),
        ('Manager', 'Manager'),
        ('HR', 'HR')
    ))

    def __str__(self):
        return self.name

    @property
    def company_name(self):
        return self.companyId.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    floor_number = models.IntegerField()

    class Meta:
        ordering = ('name',)