# Controls admin site display sees when it is logged into


# Import path to the default admin site's class
from django.contrib import admin


# Imports the djangoClasses model for display to admin site
from .models import djangoClasses

# Registers the djangoClasses model to construct a default form representation
admin.site.register(djangoClasses)
