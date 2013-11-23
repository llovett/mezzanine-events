from django.forms import ModelForm
from .models import Event, Calendar
from mezzanine.pages.admin import PageAdmin
from copy import deepcopy

class EventAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EventAdminForm, self).__init__(*args, **kwargs)

        # Only show Calendars available to use as a 'parent' instead of all Pages
        calendar = self.fields['parent']
        calendar.queryset = Calendar.objects.all()

        # Select a Calendar by default, if one exists
        all_calendars = Calendar.objects.all()
        if len(all_calendars) > 0:
            calendar.initial = all_calendars[0].id

        # Show in the side bar, but not other places
        # The initial value is dependent on PAGE_MENU_TEMPLATES
        self.fields['in_menus'].initial = [2]

    fieldsets = (
        deepcopy(PageAdmin.fieldsets[0]),
        ("Event details",{
            'fields': (
                'content', 'date',
                ('start_time', 'end_time'),
                'location', 'mappable_location',
                'parent', 'rsvp',)
        }),
        deepcopy(PageAdmin.fieldsets[1]),
    )

    class Meta:
        model = Event
        exclude = ('lat','lon',)
