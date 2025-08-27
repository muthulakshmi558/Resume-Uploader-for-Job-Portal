from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ResumeForm
from .models import Resume

def upload_resume(request):
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Resume uploaded successfully.")
            return redirect('resume_list')
    else:
        form = ResumeForm()
    return render(request, 'resumeapp/upload_resume.html', {'form': form})

def home(request):
    return render(request, "resumeapp/home.html")

def resume_list(request):
    resumes = Resume.objects.all().order_by('-uploaded_at')
    return render(request, 'resumeapp/resume_list.html', {'resumes': resumes})

def resume_detail(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'resumeapp/resume_detail.html', {'resume': resume})
