# -*- coding: utf-8 -*-

from django.conf.urls import url
import glitter_events

from . import views


calendar_urlpatterns = [
    # Calendar views
    url(
        r'^$',
        views.CalendarCurrentMonthView.as_view(),
        name='current-month'
    ),
    url(
        r'^calendar/(?P<year>\d{4})/(?P<month>\d{2})/$',
        views.CalendarMonthArchiveView.as_view(),
        name='calendar-month'
    ),

    # List views
    url(
        r'^category/(?P<slug>[-\w]+)/$',
        views.EventListCategoryView.as_view(),
        name='category-event-list'
    ),
    # Detail view
    url(
        r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/(?P<slug>[-\w]+)/$',
        views.EventDetailView.as_view(),
        name='detail'
    ),
]


events_urlpatterns = [
    # List views
    url(
        r'^$',
        views.EventListView.as_view(),
        name='event-list'
    ),
    url(
        r'^archive/$',
        views.EventListArchiveView.as_view(),
        name='event-list-archive'
    ),
    url(
        r'^category/(?P<slug>[-\w]+)/$',
        views.EventListCategoryView.as_view(),
        name='category-event-list'
    ),
    url(
        r'^category/(?P<slug>[-\w]+)/archive/$',
        views.EventListCategoryArchiveView.as_view(),
        name='category-event-list-archive'
    ),
    # Detail view
    url(
        r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/(?P<slug>[-\w]+)/$',
        views.EventDetailView.as_view(),
        name='detail'
    ),
]

if glitter_events.USE_LOCATIONS:
    events_urlpatterns.append(
        url(
            r'^location/(?P<slug>[-\w]+)/archive/$',
            views.EventListLocationArchiveView.as_view(),
            name='location-event-list'
        ),
    )


# Default to calendar urlpatterns
urlpatterns = calendar_urlpatterns

if glitter_events.USE_LOCATIONS:
    # Regardless of which pattern is chosen if we use locations, append this.
    urlpatterns.append(
        url(
            r'^location/(?P<slug>[-\w]+)/$',
            views.EventListLocationView.as_view(),
            name='location-event-list'
        ),    
    )
