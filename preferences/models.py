from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


AVAILABLE_LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
)


class Preference(models.Model):
    user = models.OneToOneField(User)
    language = models.CharField(blank=True, max_length=100, choices=AVAILABLE_LANGUAGES, default='en')

    class Meta:
        verbose_name = 'Preference'
        verbose_name_plural = 'Preferences'

    def __unicode__(self):
        return self.user.username
