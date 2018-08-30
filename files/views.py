import os
from django.utils import timezone
from django.shortcuts import render, redirect, HttpResponse
from django.views import generic
from .forms import DocumentForm
from .models import Document, CoursesNames
from django.http import HttpResponseRedirect, StreamingHttpResponse, Http404, HttpResponse
from django.urls import reverse
from django.conf import settings
from itertools import chain

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
    crs_names = CoursesNames.objects.all()
    context = {
        "crs_names": crs_names,
        "files": [],
        "not_found" : "",
    }
    if request.POST:

        file_name = request.POST["course"]
        not_found = "There is no files for {0} course yet!".format(file_name)
        documents = Document.objects.all().filter(course_name__courses__iexact=file_name)
        context["documents"] = documents
        context["filename"] = file_name

        documentObjectList = Document.objects.all().values_list("document").filter(course_name__courses__iexact=file_name)
        queryset = CoursesNames.objects.filter(courses__exact=file_name).exists()

        if queryset:
            while len(context["files"]) > 0: context["files"].pop()
            for i in documentObjectList:
                context["files"] = i
                print(context["files"])
            if len(context["documents"]) == 0: context["not_found"] = not_found
    return render(request, 'dashboard.html', context)
