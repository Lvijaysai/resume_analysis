
#resume_analysis/resumes/views.py

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Resume
from .forms import ResumeUploadForm
from .ml.analyze import analyze_resume

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()
            result = analyze_resume(resume.file.path)
            resume.parsed_text = result["raw_text"]
            resume.analysis = result
            resume.save()
            return redirect('resumes:result', pk=resume.pk)
    else:
        form = ResumeUploadForm()
    return render(request, 'resumes/upload.html', {'form': form})

def result_view(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'resumes/result.html', {'resume': resume})
