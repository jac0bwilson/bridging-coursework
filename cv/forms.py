from django import forms

from .models import Education, Skill, Experience

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = {'ed_type', 'more_detail', 'content'}

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = {'technical', 'content'}

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = {'exp_type', 'more_detail', 'content'}