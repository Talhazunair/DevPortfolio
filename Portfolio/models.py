from django.db import models

# Create your models here.
class Projects(models.Model):
    project_name = models.CharField(max_length=250)
    description = models.TextField()
    github_link = models.URLField(default="")
    demo_link = models.URLField(default="")
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.project_name