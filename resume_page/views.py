from django.shortcuts import render
from django.views import View


from .models import Author, Experience, Education, Interests, Project, Course, \
    Skill


class IndexView(View):
    def get(self, request):
        author = Author.objects.get()
        experience = Experience.objects.all().order_by('date_from').reverse()
        education = Education.objects.all().order_by('date_from').reverse()
        interests = Interests.objects.get()
        projects = Project.objects.all()
        courses = Course.objects.all().order_by('id').reverse()
        skills = Skill.objects.all()

        return render(request, "resume_page/index.html", {
            "author": author,
            "experience": experience,
            "education": education,
            "interests": interests,
            "projects": projects,
            "courses": courses,
            "skills": skills
        })
