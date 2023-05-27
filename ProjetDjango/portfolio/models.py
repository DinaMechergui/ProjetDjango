from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    description = models.TextField()
    services = models.CharField(max_length=200)
    completion_date = models.DateField()
    Img=models.ImageField(blank=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images')
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description
