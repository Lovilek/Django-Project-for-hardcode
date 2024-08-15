from django.contrib import admin

from courses.models import Course, Lesson, Group

admin.site.register(Course)
admin.site.register(Lesson)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('course',)
    filter_horizontal = ('students',)


admin.site.register(Group, GroupAdmin)
