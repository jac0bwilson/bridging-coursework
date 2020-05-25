from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import EducationForm, SkillForm, ExperienceForm, ProjectForm
from .models import Education, Skill, Experience, Project

# Create your views here.
def cv_page(request):
    education = Education.objects.all()
    skills = Skill.objects.all()
    experience = Experience.objects.all()
    projects = Project.objects.all()
    return render(request, 'cv/cv.html', {'education': education, 'skills': skills, 'experience': experience, 'projects': projects})

@login_required
def cv_new_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.save()
            return redirect('/cv/')
    else:
        form = EducationForm()
    return render(request, 'cv/new_education.html', {'form': form})

@login_required
def cv_new_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.save()
            return redirect('/cv/')
    else:
        form = SkillForm()
    return render(request, 'cv/new_skill.html', {'form': form})

@login_required
def cv_new_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.save()
            return redirect('/cv/')
    else:
        form = ExperienceForm()
    return render(request, 'cv/new_experience.html', {'form': form})

@login_required
def cv_new_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('/cv/')
    else:
        form = ProjectForm()
    return render(request, 'cv/new_project.html', {'form': form})