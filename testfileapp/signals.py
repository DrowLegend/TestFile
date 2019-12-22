from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import UploadFile
from .tasks import set_status_as_inactive


@receiver(post_save, sender=UploadFile)
def notify(sender, instance, created, **kwargs):
    if created:
        set_status_as_inactive.delay(instance.pk)