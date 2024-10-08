from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Home, WhyUs, Services, Suggestions, OurService, Portfolio, ContactInfo, About, Team, Contact, \
    Category, Connection, CustomerOpinion


class AboutAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title', 'description')


class TeamAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'surname', 'profession')
    list_display_links = ('id', 'name', 'surname', 'profession')


class ConnectionAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'surname', 'phone', 'opinion')
    list_display_links = ('id', 'name', 'surname', 'phone', 'opinion')


admin.site.register(Home)
admin.site.register(WhyUs)
admin.site.register(Services)
admin.site.register(Suggestions)
admin.site.register(OurService)
admin.site.register(Portfolio)
admin.site.register(ContactInfo)
admin.site.register(About, AboutAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Contact)
admin.site.register(Connection, ConnectionAdmin)
admin.site.register(Category)
admin.site.register(CustomerOpinion)
