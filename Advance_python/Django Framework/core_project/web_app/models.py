from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    # Define the columns for the database table
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[('Active', 'Active'), ('On Leave', 'On Leave')],
        default='Active'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name