from django.urls import path

from .views import FileUploadAPI, FileMergeAPI, DownloadOutputFileAPI

urlpatterns = [
    path('upload/', FileUploadAPI.as_view()),
    path('file-merge/<int:session_id>', FileMergeAPI.as_view()),
    path('file-download/<int:session_id>', DownloadOutputFileAPI.as_view())
]
