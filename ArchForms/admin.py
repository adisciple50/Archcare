from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(StaffMember)
admin.site.register(ServiceUser)
admin.site.register(ProgressReport)
admin.site.register(WeeklyReport)

