from django.db import models

# Create your models here.

class TechStack(models.Model):
    stack = models.CharField(max_length=256)

class PortfolioProject(models.Model):
    title = models.CharField(max_length=256)
    screenshot = models.URLField()
    repository = models.URLField()
    live_link = models.URLField()
    tech_stack = models.ForeignKey(TechStack, on_delete=models.PROTECT, related_name="tech_stack_used")
    description = models.TextField()