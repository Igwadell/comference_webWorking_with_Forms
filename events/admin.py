from django.contrib import admin
from events.models import Event, Category, Schedule, Participant, Reminder, Report, Payment

# Register your models here.
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Schedule)
admin.site.register(Participant)
admin.site.register(Reminder)
admin.site.register(Report)
admin.site.register(Payment)