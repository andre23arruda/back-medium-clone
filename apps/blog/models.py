from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.api import APIField
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.images.api.fields import ImageRenditionField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class ArticleTag(TaggedItemBase):
    content_object = ParentalKey(
        'Article',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class Article(Page):
    published_at = models.DateField()
    thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=ArticleTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('published_at'),
        ImageChooserPanel('thumbnail'),
        FieldPanel('intro'),
        FieldPanel('tags'),
        FieldPanel('body', classname="full"),
    ]

    api_fields = [
        APIField('published_at'),
        APIField('intro'),
        APIField('body'),
        APIField('tags'),
        APIField('thumbnail'),
        APIField('feed_thumbnail', serializer=ImageRenditionField('fill-100x100', source='thumbnail')),
    ]
# http://127.0.0.1:8000/api/pages/?type=blog.Article&fields=published_at,intro,body,tags,thumbnail,feed_thumbnail