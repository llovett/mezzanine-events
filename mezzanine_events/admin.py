from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Event, Calendar
from .forms import EventAdminForm
from copy import deepcopy

class MezzanineEventsAdmin(admin.ModelAdmin):
        app_label = "Events"

class EventAdmin (MezzanineEventsAdmin):
        form = EventAdminForm

class CalendarAdmin(MezzanineEventsAdmin):
        pass

admin.site.register(Event, EventAdmin)
admin.site.register(Calendar, CalendarAdmin)
