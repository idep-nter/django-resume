from django.contrib import admin

from .models import Author, Experience, Education, Interests, Project, Course, \
    Skill

admin.site.register(Author)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Interests)
admin.site.register(Project)
admin.site.register(Course)
admin.site.register(Skill)