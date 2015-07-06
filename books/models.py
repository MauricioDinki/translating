from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

CATEGORY = (
    ('maths', _('Maths')),
    ('science', _('Science')),
    ('biology', _('Biology')),
    ('geography', _('Geography')),
)


class Book(models.Model):
    name = models.CharField(blank=True, max_length=100)
    category = models.CharField(blank=True, max_length=100, choices=CATEGORY)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Book, self).save(*args, **kwargs)
