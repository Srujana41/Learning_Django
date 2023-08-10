from django.contrib import admin
from .models import Task

# To change the view on admin page to view details on database page instead of going into details page
# To also add search field to go through data
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_Completed', 'updated_at')
    search_fields = ('task',)


# Register your models here.
#added TaskAdmin to change admin page
admin.site.register(Task, TaskAdmin)
