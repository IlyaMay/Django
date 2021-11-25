from django.db import models
from django.urls import reverse

# Create your models here.

class TWEET(models.Model):
    title = models.CharField(max_length=400, verbose_name='Заголовок')
    text = models.CharField(max_length=400, verbose_name="Текст")
    img = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Изображение')
    time_crate = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')


    class Meta:
        verbose_name_plural = "Посты"
        ordering = ['-time_crate']

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.pk})