from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(blank=True, max_length=100)
    last_name = models.CharField(blank=True, max_length=100)
    birth_day = models.DateField()
    biography = models.CharField(blank=True, max_length=100)

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        full_name = '%s %s' % (self.first_name, self.last_name)
        self.slug = slugify(full_name)
        super(Author, self).save(*args, **kwargs)
