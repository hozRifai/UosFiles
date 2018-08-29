from rest_framework import serializers 

from files.models import Document 
class DocumentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document 
        fields = [
            "courses",
            "description", 
            "document",
            "uploaded_at"
        ]