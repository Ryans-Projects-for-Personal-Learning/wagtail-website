from multiprocessing import Event
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from .models import GenericPage

class GenericPageAdmin(ModelAdmin):
    model = GenericPage
    menu_label = "Generic Pages"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False

modeladmin_register(GenericPageAdmin)