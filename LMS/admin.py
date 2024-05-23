from django.contrib import admin
from .models import Course, Section

class SectionInline(admin.TabularInline):
    model = Section
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [SectionInline]
    list_display = ('title',)
    search_fields = ('title', 'description')

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    fields = ('course', 'title', 'description', 'video', 'order')
    search_fields = ('title', 'course__title')
    list_filter = ('course',)
