from django.db import models


# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FileLink(TimeStamp):
    file = models.FileField()


class UserSession(TimeStamp):
    input_files = models.ManyToManyField(FileLink, through='pdf.SessionFileLink')
    output_file = models.OneToOneField(FileLink, on_delete=models.SET_NULL, null=True, related_name='user_session')


class SessionFileLink(TimeStamp):
    session = models.ForeignKey(UserSession, on_delete=models.CASCADE)
    file = models.ForeignKey(FileLink, on_delete=models.SET_NULL, null=True, related_name='session_file_links')
