from rest_framework import generics , mixins 
from files.models import Document
from .serializers import DocumentPostSerializer


class FileRUDDocument(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "document"
    serializer_class = DocumentPostSerializer

    def get_queryset(self):
        return Document.objects.all()


class UploadDocument(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = "document"
    serializer_class = DocumentPostSerializer

    def get_queryset(self):
        return Document.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)