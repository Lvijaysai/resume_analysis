
# Create your models here.
#resume_analysis/resumes/models.py
from django.db import models

# Create your models here.
class Resume(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='resumes/')
    parsed_text = models.TextField(blank=True)
    analysis = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.file.name