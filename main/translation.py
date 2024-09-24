from modeltranslation.translator import TranslationOptions, translator
from .models import About, Team, ContactInfo, Services, Suggestions, OurService, Home, WhyUs, Portfolio, Contact


# @register(Post)
class HomeTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'image',)


class TeamTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'profession', 'image')


class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'image')


class ContactTranslationOptions(TranslationOptions):
    fields = ('name', 'email', 'website', 'message')


translator.register(Home, HomeTranslationOptions)
translator.register(Team, TeamTranslationOptions)
translator.register(About, AboutTranslationOptions)
translator.register(Contact, ContactTranslationOptions)
translator.register(ContactInfo)
translator.register(Services)
translator.register(OurService)
translator.register(Suggestions)
translator.register(WhyUs)
translator.register(Portfolio)
