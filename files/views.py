import os
from django.utils import timezone
from django.shortcuts import render, redirect, HttpResponse
from django.views import generic
from .forms import DocumentForm
from .models import Document, CoursesNames
from django.http import HttpResponseRedirect, StreamingHttpResponse, Http404, HttpResponse
from django.urls import reverse
from django.conf import settings


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
    }
    """ a way to download my files by accessing the files through the system """
    if request.POST:
        file_name = request.POST["course"]
        context["filename"] = file_name

        not_found = "There is no files for {0} course yet!".format(file_name)
        documents = Document.objects.all().filter(course_name__courses__iexact=file_name)
        context["documents"] = documents
        print(documents)
        queryset = CoursesNames.objects.filter(courses__exact=file_name).exists()



        if queryset:
            # in case we have't found the directory of the file
            error_to_catch = getattr(
                __builtins__, 'FileNotFoundError', IOError)
            try:
                directory = settings.MEDIA_ROOT+"/documents/"+file_name+"/"
                contents = os.listdir(directory)
            except error_to_catch:
                context["not_found"] = not_found
                return render(request, 'dashboard.html', context)
            # append the files under the course directory to the files list
            for item in contents:
                if os.path.isfile(os.path.join(directory, item)):
                    context["files"].append(item)
    return render(request, 'dashboard.html', context)
