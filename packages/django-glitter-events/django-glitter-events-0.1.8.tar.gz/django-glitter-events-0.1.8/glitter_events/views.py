# -*- coding: utf-8 -*-

import datetime

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.dates import DateDetailView, MonthArchiveView
from glitter.mixins import GlitterDetailMixin

from .mixins import CalendarMixin, CategoryMixin, EventsMixin, EventsQuerysetMixin, LocationMixin
from .models import Category, Event, Location


class EventDetailView(GlitterDetailMixin, EventsMixin, DateDetailView):
    model = Event
    month_format = '%m'
    date_field = 'date_url'
    allow_future = True

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['current_category'] = self.object.category
        return context


class BaseCalendarMonthView(CalendarMixin, EventsMixin, MonthArchiveView):
    def get_queryset(self):
        qs = super(BaseCalendarMonthView, self).get_queryset()
        return qs.order_by('start')


class CalendarCurrentMonthView(BaseCalendarMonthView):
    def get_year(self):
        return str(timezone.now().year)

    def get_month(self):
        return str(timezone.now().month)


class CalendarMonthArchiveView(BaseCalendarMonthView):
    pass


class BaseEventListView(EventsQuerysetMixin, EventsMixin, ListView):
    paginate_by = 10


class EventListView(BaseEventListView):
    def get_queryset(self):
        qs = super(EventListView, self).get_queryset()
        today = datetime.datetime.combine(date=datetime.date.today(), time=datetime.time.min)
        today = timezone.make_aware(today)
        return qs.filter(start__gte=today)


class EventListArchiveView(BaseEventListView):
    template_name_suffix = '_list_archive'

    def get_queryset(self):
        qs = super(EventListArchiveView, self).get_queryset()
        today = datetime.datetime.combine(date=datetime.date.today(), time=datetime.time.min)
        today = timezone.make_aware(today)
        return qs.filter(start__lt=today).order_by('-start')


class EventListCategoryView(CategoryMixin, EventListView):
    template_name_suffix = '_list_category'

    def get_queryset(self):
        """
        Categories such as 'all events' should return all categories, not just
        the events with category__title='all_events'. The name of this type of
        category could change for each separate site so a settings variable has
        been introduced so it can be set on a per-site basis.
        If the title of the given category matches the ALL_EVENTS_CATEGORY_TITLE for
        the site, all events will be returned, otherwise, the category filter
        will be applied as normal.
        """
        qs = super(EventListCategoryView, self).get_queryset()
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        if hasattr(settings, 'ALL_EVENTS_CATEGORY_TITLE'):
            if self.category.title == settings.ALL_EVENTS_CATEGORY_TITLE:
                return qs
        return qs.filter(category=self.category)


class EventListCategoryArchiveView(CategoryMixin, EventListArchiveView):
    template_name_suffix = '_list_category_archive'

    def get_queryset(self):
        qs = super(EventListCategoryArchiveView, self).get_queryset()
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return qs.filter(category=self.category)


class EventListLocationView(LocationMixin, EventListView):
    template_name_suffix = '_list_location'

    def get_queryset(self):
        qs = super(EventListLocationView, self).get_queryset()
        self.location = get_object_or_404(Location, slug=self.kwargs['slug'])
        return qs.filter(locations=self.location)


class EventListLocationArchiveView(LocationMixin, EventListArchiveView):
    template_name_suffix = '_list_location_archive'

    def get_queryset(self):
        qs = super(EventListLocationArchiveView, self).get_queryset()
        self.location = get_object_or_404(Location, slug=self.kwargs['slug'])
        return qs.filter(locations=self.location)
