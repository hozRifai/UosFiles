from django import forms
from .models import Document , CoursesNames

class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ('course_name','title' ,  'description', 'document',  )

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


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')