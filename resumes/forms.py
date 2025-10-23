
#resume_analysis/resumes/forms.py
from django import forms
from .models import Resume
from django.core.exceptions import ValidationError

ALLOWED_EXTENSIONS = ['.pdf', '.docx', '.doc', '.txt']

def validate_file_extension(file):
    import os
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValidationError(f'Unsupported file extension: {ext}. Allowed: {ALLOWED_EXTENSIONS}')

def validate_file_size(file):
    max_size = 5 * 1024 * 1024  # 5 MB
    if file.size > max_size:
        raise ValidationError(f'File too large. Maximum allowed: 5MB')

class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['file']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        validate_file_extension(file)
        validate_file_size(file)
        return file

