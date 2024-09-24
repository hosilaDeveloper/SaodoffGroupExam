from django.urls import path
from .views import HomeList, WhyUsView, ContactView, ContactInfoView, PortfolioView, ServiceView, SuggestionsView, \
    OurServiceView, AboutView, TeamView

urlpatterns = [
    path('', HomeList.as_view(), name='home-list'),
    path('about/', AboutView.as_view(), name='about-list'),
    path('team/', TeamView.as_view(), name='team-list'),
    path('service/', ServiceView.as_view(), name='service-list'),
    path('ourService/', OurServiceView.as_view(), name='our-service'),
    path('whyUs/', WhyUsView.as_view(), name='why-Us'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio-list'),
    path('suggestion/', SuggestionsView.as_view(), name='suggestion-list'),
    path('contact', ContactView.as_view(), name='contact-list'),
    path('info/', ContactInfoView.as_view(), name='contact-info'),
]
