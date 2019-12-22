from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UploadFile(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Автор файла')
    file = models.FileField(verbose_name='Название файла')
    is_active = models.BooleanField(default='False', verbose_name='Статус загрузки файла')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки файла')

    def __str__(self):
        return f'{self.file.name} by {self.author}'

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ['-date']



