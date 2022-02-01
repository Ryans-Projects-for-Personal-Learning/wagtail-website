from email.policy import default
from django.db import models

from wagtail.core.models import Page

from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

import datetime


# Create your models here.

class NewsPostList(Page):

    template = "news/news_post_list.html"

    def get_context(self, request, *args, **kwargs):

        context = super().get_context(request, *args, **kwargs)
        context["posts"] = NewsPost.objects.live().public()

        return context

class NewsPost(Page):

    news_date = models.DateField("Post date",default=datetime.date.today)

    news_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name = "+",
        on_delete=models.SET_NULL,
        help_text="This is the thumbnail for the news article."
    )

    body = RichTextField(default="")

    content_panels = Page.content_panels + [
        FieldPanel('news_date'),
        ImageChooserPanel('news_image'),
        FieldPanel('body')
    ]