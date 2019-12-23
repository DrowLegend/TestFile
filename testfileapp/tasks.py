from celery import shared_task
from testfileapp.models import UploadFile
import time

# таск запускается по сигналу с signal.py
@shared_task
def set_status_as_inactive(pk):
    file = UploadFile.objects.get(pk=pk)
    time.sleep(3)
    file.is_active = True
    file.save()


