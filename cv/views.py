from django.shortcuts import render, redirect

from .forms import EducationForm
from .models import Education

# Create your views here.
def cv_page(request):
    education = Education.objects.all()
    return render(request, 'cv/cv.html', {'education': education})

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