# Import of django models provides built-in features that Django uses
# to create tables, their fields, sets various constraints
from django.db import models


# University class model database mapping schema that details course fields,
# data types, and data field parameters
class djangoClasses(models.Model):
    Title = models.CharField(max_length=75, default="", blank=True, null=False)
    Course_Number = models.IntegerField(unique=True, default="", blank=True, null=False)
    Instructor_Name = models.CharField(max_length=75, default="", blank=True, null=False)
    Duration = models.DecimalField(max_digits=5, decimal_places=2)

# Interface between model code and the database backend
    objects = models.Manager()

# Method is called when print() or str() function is invoked on an object
# Dictates the course display name in the web browser (i.e., Geopolitical Studies)
    def __str__(self):
        return self.Title



