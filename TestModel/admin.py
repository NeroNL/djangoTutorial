# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from TestModel.models import Test, Contact, Tag
from django.contrib import admin


# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',),
            'fields': ('age',),
        }]

    )



admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
