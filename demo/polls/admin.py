from polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None, 
            {'fields': ['question']}),
        ('Date information', 
            {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)