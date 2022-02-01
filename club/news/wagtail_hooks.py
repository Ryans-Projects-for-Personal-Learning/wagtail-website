from multiprocessing import Event
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from .models import NewsPost

class NewsPostAdmin(ModelAdmin):
    model = NewsPost
    menu_label = "News Posts"
    menu_order = 300
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title','news_date')
    search_fields = ('title')

modeladmin_register(NewsPostAdmin)