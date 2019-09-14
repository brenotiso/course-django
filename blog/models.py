from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField
from curso.settings import AUTH_USER_MODEL


class Publication(models.Model):
    title = models.CharField('Título', max_length=100)
    subtitle = models.CharField('Título', max_length=200)
    text = HTMLField('Texto')
    author = models.ForeignKey(AUTH_USER_MODEL, verbose_name='Autor', on_delete=models.PROTECT)
    date = models.DateTimeField('Data', auto_now=True)

    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicação'

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT)
    comment = models.TextField('Comentário')
    publication = models.ForeignKey(Publication, verbose_name='Publicação', related_name='comments', on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return 'Comentário de {}'.format(self.user.first_name)
