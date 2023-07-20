from django.urls import path
from .views import event_list, event_details, event_schedules
## , participant_list
# from . import views
urlpatterns = [
    path('', event_list, name='event_list'),
    path('<str:title>/', event_details, name='event_details'),
    path('<int:event_id>/schedules/', event_schedules, name='event_schedules'),

    # path('participants/', participant_list, name='participant_list'),



#######################################
#------------------------------------
    # 1.path('events/', views.event_list, name='event_list'),
    #   path('detail/<str:title>/', views.event_details, name='event_detail'),
    
    # path('participants/<str:email>/', views.participant_detail, name='participant_detail'),
    # path('schedules/', views.schedule_list, name='schedule_list'),

    #2.

    # path('schedules/<int:event_id>/', views.event_schedules, name='event_schedules'),
    # path('payments/', views.payment_list, name='payment_list'),

    #3.

    # path('payments/<str:email>/', views.participant_payments, name='participant_payments'),
    # path('upcoming/', views.upcoming_events, name='upcoming_events'),
    # path('free/', views.free_events, name='free_events'),

    #4. 

    # path('paid/', views.paid_events, name='paid_events'),
    # path('participant-count/', views.event_participant_count, name='event_participant_count'),
    
    #5.

    # path('event-attendance-count/', views.participant_event_count, name='participant_event_count'),
    # path('schedule-count/', views.event_schedule_count, name='event_schedule_count'),
    # path('total-payment/<int:event_id>/', views.event_total_payment, name='event_total_payment'),
    
    #6.

    # path('average-price-paid-events/', views.average_price_paid_events, name='average_price_paid_events'),
    # path('event-participants/<int:event_id>/', views.event_participants, name='event_participants'),
    # path('event-speakers/<int:event_id>/', views.event_speakers, name='event_speakers'),
    
    #7
    # path('events-in-date-range/<str:start_date>/<str:end_date>/', views.events_in_date_range, name='events_in_date_range'),
    # path('participants-attended-all/', views.participants_attended_all_events, name='participants_attended_all_events'),
    # path('events-without-speakers/', views.events_without_speakers, name='events_without_speakers'),
    
    #8
    # path('highest-paid-events/', views.highest_paid_events, name='highest_paid_events'),
    # path('participants-highest-payment/', views.participants_highest_payment, name='participants_highest_payment'),
    # path('speakers-most-scheduled-events/', views.speakers_most_scheduled_events, name='speakers_most_scheduled_events'),
    
    
    #9

    # path('events-longest-duration/', views.events_longest_duration, name='events_longest_duration'),
    # path('participants-most-events-in-month/<int:month>/', views.participants_most_events_in_month, name='participants_most_events_in_month'),
    # path('events-with-overlapping-schedules/', views.events_with_overlapping_schedules, name='events_with_overlapping_schedules'),
    
    #10

    # path('participants-recent-payment/', views.participants_recent_payment, name='participants_recent_payment'),
    # path('participants-attended-consecutive-events/', views.participants_attended_consecutive_events, name='participants_attended_consecutive_events'),
    # path('speakers-without-events/', views.speakers_without_events, name='speakers_without_events'),
    
    
    #11
    
    # path('events-highest-total-payment/', views.events_highest_total_payment, name='events_highest_total_payment'),
    # path('participants-multiple-locations/', views.participants_multiple_locations, name='participants_multiple_locations'),
    # path('speakers-different-topics/', views.speakers_different_topics, name='speakers_different_topics'),
    
    #12
    
    # path('events-longest-gap/', views.events_longest_gap, name='events_longest_gap'),
    # path('participants-by-location/<str:location>/', views.participants_by_location, name='participants_by_location'),
    # path('speakers-highest-average-rating/', views.speakers_highest_average_rating, name='speakers_highest_average_rating'),
    # path('participants-all-payments/', views.participants_all_payments, name='participants_all_payments'),
#------------------------------------
#######################################




]
