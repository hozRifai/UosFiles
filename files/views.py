import os
from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render , redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Document, CoursesNames
from .forms import DocumentForm  , ContactForm


def model_form_upload(request):
    """ a simple form to upload the files """
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.uploaded_at = timezone.now()
            file.save()
            return HttpResponseRedirect(reverse('files:dashboard'))
    else:
        form = DocumentForm()
    context = {
        "form": form,
    }
    return render(request, 'documents.html', context)


def showDocuments(request, *args, **kwargs):
    """ shows all the files of the requested course  """
    crs_names = CoursesNames.objects.all().order_by('courses')
    context = {
        "crs_names": crs_names,
        "files": [],
        "not_found" : "",
    }
    if request.POST:

        file_name = request.POST["course"]
        not_found = "There are no files for {0} yet!".format(file_name)
        documents = Document.objects.all().filter(course_name__courses__iexact=file_name)
        context["documents"] = documents
        context["filename"] = file_name
        #list of document and not a query
        documentObjectList = Document.objects.all().values_list("document").filter(course_name__courses__iexact=file_name)
        queryset = CoursesNames.objects.filter(courses__exact=file_name).exists()

        if queryset:
            while len(context["files"]) > 0: context["files"].pop()
            for i in documentObjectList:
                context["files"] = i
                print(context["files"])
            if len(context["documents"]) == 0: context["not_found"] = not_found
    return render(request, 'dashboard.html', context)


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ["houzayfalistening@gmail.com"])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/')
    return render(request, "contact-us.html", {'form': form})
