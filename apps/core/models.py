from django.db import models
from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig

class CoreConfig(AppConfig):
    name = 'core'
    verbose_name = _(u"Основное")


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Последнее обновление'))

    class Meta:
        abstract = True