from PyPDF2 import PdfFileMerger
from django.db import transaction
from django.http import HttpResponse
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
import base64

from .models import UserSession, FileLink
from .serializers import FileUploadSerializer


# Create your views here.

class FileUploadAPI(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileUploadSerializer

    def post(self, request):
        files_list = request.FILES.getlist('files')
        with transaction.atomic():
            session = UserSession.objects.create()
            for file in files_list:
                data = {'file': file}
                serializer = self.serializer_class(data=data, context={'session': session})
                serializer.is_valid(raise_exception=True)
                serializer.save()
        return Response({'session': session.id}, status=status.HTTP_201_CREATED)


class FileMergeAPI(APIView):

    def get(self, request, session_id):
        merger = PdfFileMerger()
        output_file = str(session_id) + '.pdf'
        session = UserSession.objects.get(id=session_id)
        session_file_links = FileLink.objects.filter(session_file_links__session=session)
        if session_file_links:
            for file_link in session_file_links:
                merger.append(file_link.file)
        merger.write(output_file)
        output_file_link = FileLink.objects.create(file=output_file)
        session.output_file = output_file_link
        session.save()
        return Response('Merged SuccessFully')


class DownloadOutputFileAPI(APIView):

    def get(self, request, session_id):
        filename = str(session_id) + '.pdf'
        file = open(filename, 'rb')
        response = HttpResponse(file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={filename}'
        return response
