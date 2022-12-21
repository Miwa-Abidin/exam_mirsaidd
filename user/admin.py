from django.contrib import admin


from . import models

admin.site.register(models.Student)
admin.site.register(models.Language)
admin.site.register(models.Mentor)
admin.site.register(models.Course)
