from django.db import models
from django.utils.translation import ugettext as _



class Articles(models.Model):
    title = models.CharField(_(u'Title'), max_length=50, null=False, blank=False)
    url = models.SlugField(_(u'URL'), max_length=50, unique=True)
    text = models.TextField(_(u'Text'), null=False, blank=False)
    created = models.DateTimeField( _(u'Created'), auto_now_add=True)
    lastModify = models.DateTimeField( _(u'Last modify'), auto_now=True)

    def __repr__(self):
        return '<Article: %s>' % self.title

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['created']

