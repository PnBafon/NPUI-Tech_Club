from django.db import models

# Create your models here.

class Applications(models.Model):
    name = models.CharField(max_length=100,)
    matricule = models.CharField(max_length=50)
    # links = 
    email = models.EmailField()
    github = models.URLField()
    projects = models.OneToOneField("Links", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Specialization(models.Model):
    name = models.CharField(max_length=30)
    applicants = models.ForeignKey(Applications, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Links(models.Model):
    matricule = models.CharField(unique=True, max_length=50)
    project_1 = models.URLField(null=True, blank=True)
    project_2 = models.URLField(null=True, blank=True)
    project_3 = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.matricule