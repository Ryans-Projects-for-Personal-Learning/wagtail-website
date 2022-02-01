from email.policy import default
from django.db import models
from django.forms import MultiValueField

from wagtail.core.models import Page

from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from wagtail.snippets.models import register_snippet

import datetime


# Create your models here.

@register_snippet
class EventCategory(models.Model):
    event_category = models.CharField(max_length=100, null=False,blank=False)
    
    #Field for adding new panels
    panels = [ 
                FieldPanel("event_category")
            ]
    
    class Meta:
        verbose_name = "Event Category"
        verbose_name_plural = "Event Categories"

    def __str__(self):
        return self.event_category

class EventPostList(Page):

    template = "events/event_list.html"

    def get_context(self, request, *args, **kwargs):

        context = super().get_context(request, *args, **kwargs)
        context["posts"] = EventPost.objects.live().public()

        return context

class EventPost(Page):

    event_date = models.DateField("Event Date",default=datetime.date.today)

    event_time = models.TimeField()

    event_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name = "+",
        on_delete=models.SET_NULL,
        help_text="This is the thumbnail for the event page."
    )

    event_category = models.ForeignKey(
        EventCategory,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+")

    body = RichTextField(default="")

    content_panels = Page.content_panels + [
        SnippetChooserPanel('event_category'),
        FieldPanel('event_date'),
        FieldPanel('event_time'),
        ImageChooserPanel('event_image'),
        FieldPanel('body')
    ]

