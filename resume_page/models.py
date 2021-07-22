from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    email_address = models.EmailField()
    about_me = models.TextField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(blank=True, max_length=100)
    date_from = models.CharField(max_length=50)
    date_to = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta():
        verbose_name_plural = "Experience"

    def __str__(self):
        return f"{self.title}"


class Education(models.Model):
    title = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    date_from = models.CharField(max_length=50)
    date_to = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta():
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.title}"


class Project(models.Model):
    title = models.CharField(max_length=100)
    github_link = models.CharField(max_length=100)
    about = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title}"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"


class Course(models.Model):
    title = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    date_from = models.CharField(max_length=50)
    date_to = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title}"



class Interests(models.Model):
    content = models.TextField()

    class Meta():
        verbose_name_plural = "Interests"