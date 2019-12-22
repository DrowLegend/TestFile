from celery import shared_task
#from .models import UploadFile

@shared_task
def set_status_as_inactive(pk):
    UploadFile.objects.get(pk=pk)
