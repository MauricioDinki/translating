from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from authors.models import Author

CATEGORY = (
    ('maths', _('Maths')),
    ('science', _('Science')),
    ('biology', _('Biology')),
    ('geography', _('Geography')),
)


class Book(models.Model):
    name = models.CharField(blank=True, max_length=100)
    category = models.CharField(blank=True, max_length=100, choices=CATEGORY)
    description = models.CharField(blank=True, max_length=100)
    author = models.ForeignKey(Author)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Book, self).save(*args, **kwargs)
