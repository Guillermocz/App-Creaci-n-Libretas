from django.contrib import admin
from .models import ReportCard, Grade

class GradeInline(admin.TabularInline):
    model = Grade
    extra = 1

class ReportCardAdmin(admin.ModelAdmin):
    inlines = [GradeInline]
    list_display = ('student', 'course', 'created_at')
    search_fields = ('student__nombre_completo', 'course__nombre_de_curso')

admin.site.register(ReportCard, ReportCardAdmin)
# Register your models here.
