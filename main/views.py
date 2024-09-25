from rest_framework import generics
from .models import About, Team, ContactInfo, Services, Suggestions, OurService, Home, WhyUs, Portfolio, Contact, \
    Connection, CustomerOpinion, Category
from .serializers import AboutSerializer, TeamSerializer, ContactInfoSerializer, ServiceSerializer, \
    SuggestionsSerializer, OurServiceSerializer, HomeSerializer, WhyUsSerializer, PortfolioSerializer, \
    ContactSerializer, CategorySerializer, ConnectionSerializer, CustomerOpinionSerializer


class HomeList(generics.ListCreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class AboutView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class TeamView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ServiceView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer


class OurServiceView(generics.ListAPIView):
    queryset = OurService.objects.all()
    serializer_class = OurServiceSerializer


class SuggestionsView(generics.ListAPIView):
    queryset = Suggestions.objects.all()
    serializer_class = SuggestionsSerializer


class WhyUsView(generics.ListAPIView):
    queryset = WhyUs.objects.all()
    serializer_class = WhyUsSerializer


class PortfolioView(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class ContactInfoView(generics.ListAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer


class ContactView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ConnectionView(generics.ListAPIView):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer


class CustomerOpinionView(generics.ListAPIView):
    queryset = CustomerOpinion.objects.all()
    serializer_class = CustomerOpinionSerializer
