from django.contrib import admin

from .models import Choice, Poll



class ChoiceInline(admin.StackedInline):
    model = Choice


#class PollAdmin(admin.ModelAdmin):
#   inlines = (ChoiceInline,)

    
admin.site.register(Poll)
admin.site.register(Choice)
