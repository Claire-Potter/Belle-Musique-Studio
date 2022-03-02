""".git/"""
from django.contrib import admin
from .models import Lesson, Type


class LessonAdmin(admin.ModelAdmin):
    """.git/"""
    list_display = (
        'sku',
        'name',
        'type',
    )

    ordering = ('sku',)


class LessonTypeAdmin(admin.ModelAdmin):
    """.git/"""
    list_display = (
        'call_type',
        'type',
    )


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Type, LessonTypeAdmin)

