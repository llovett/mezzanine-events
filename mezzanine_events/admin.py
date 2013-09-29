from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Event, Calendar
from copy import deepcopy

# event_admin_fieldsets = deepcopy(PageAdmin.fieldsets)
# event_admin_fieldsets[0][1]["fields"]

class MezzanineEventsAdmin(admin.ModelAdmin):
        app_label = "Events"

class EventAdmin (MezzanineEventsAdmin):
	fieldsets = (
		deepcopy(PageAdmin.fieldsets[0]),
		("Event details",{
			'fields': ('content', 'date', ('start_time', 'end_time'), 'location', 'mappable_location', ('lat', 'lon'), 'rsvp')
                        }),
		deepcopy(PageAdmin.fieldsets[1]),
	)

class CalendarAdmin(MezzanineEventsAdmin):
        pass
        
admin.site.register(Event, EventAdmin)
admin.site.register(Calendar, CalendarAdmin)
