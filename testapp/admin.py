from django.contrib import admin
from testapp.models import Employee
# Register your models here.
class EmployeAdmin(admin.ModelAdmin):
    list_display=['ename','eno','esal','eaddr']

admin.site.register(Employee,EmployeAdmin)
