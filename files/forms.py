from django import forms
from .models import Document , CoursesNames

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title' ,  'description', 'document','course_name',  )

    def clean_title(self):
        title = self.cleaned_data.get('title')
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description')
        return description

    def clean_document(self):
        document = self.cleaned_data.get('document')
        return document

    def clean_course_name(self):
        course_name = self.cleaned_data.get('course_name')
        return course_name

class CoursesNamesForm(forms.ModelForm):

    class Meta:
        model = CoursesNames
        fields = ('courses',)
        verbose_name_plural = "Courses"

    def clean_courses(self):
        courses = self.cleaned_data.get('courses')
        return courses