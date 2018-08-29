from django.urls import path , include , re_path
from .views import FileRUDDocument  , UploadDocument

urlpatterns = [
    re_path(r'^(?P<pk>\d+)/$', FileRUDDocument.as_view() , name="post_files"),
    path("" , UploadDocument.as_view() , name = "upload_document")
]
