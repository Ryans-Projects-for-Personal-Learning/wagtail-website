from multiprocessing import Event
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from .models import EventPost

class EventPostAdmin(ModelAdmin):
    model = EventPost
    menu_label = "Events"
    menu_order = 300
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title','event_date','event_time','event_category')
    search_fields = ('title')

modeladmin_register(EventPostAdmin)