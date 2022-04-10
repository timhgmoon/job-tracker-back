from django.db import models
from django.contrib.auth import get_user_model

class Job(models.Model):
  class AppProcess(models.TextChoices):
    INTERESTED = 'interested'
    APPLIED = 'applied'
    INTERVIEWING = 'interviewing'
    OFFER = 'offer'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
  app_process = models.CharField(
    max_length = 30,
    choices = AppProcess.choices,
    default=AppProcess.INTERESTED
  )
  company = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  job_title = models.CharField(max_length=100)
  salary = models.IntegerField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.company} {self.location} {self.salary} {self.AppProcess}"