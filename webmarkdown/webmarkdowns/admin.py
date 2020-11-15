from django.contrib import admin

# Register your models here.

from .models import Projects, Articles

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'project_name')

class  ArticlesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'project', 'owner', 'time_stamp', 'markdown_txt')


admin.site.register(Projects,  ProjectsAdmin)
admin.site.register(Articles, ArticlesAdmin)

