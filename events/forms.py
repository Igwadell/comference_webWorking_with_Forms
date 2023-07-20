from django.forms import ModelForm
from events.models import Event

# Create the form class.
class EventForm (ModelForm):
         class Meta:
             model = Event
             fields = ["title", "description", "start_date","end_date", "location","category","is_free"]

# form = EventFrom()