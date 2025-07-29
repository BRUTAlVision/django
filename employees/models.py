from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="First Name")
    last_name = models.CharField(max_length=30, verbose_name="Last Name")
    email = models.EmailField(max_length=100, unique=True, verbose_name="Email Address")
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Photo")
    designation = models.CharField(max_length=50, verbose_name="Designation")
    department = models.CharField(max_length=50, verbose_name="Department")
    date_of_joining = models.DateField(verbose_name="Date of Joining")
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Phone Number")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.designation}"
