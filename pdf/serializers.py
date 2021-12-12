from rest_framework import serializers

from .models import FileLink, SessionFileLink


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False)

    def create(self, data):
        file = data.get('file')
        session = self.context.get('session')
        if file:
            file_obj = FileLink.objects.create(file=file)
            SessionFileLink.objects.create(file=file_obj, session=session)
            return session.id
        else:
            return {"files": file}
