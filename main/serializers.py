from rest_framework import serializers
from .models import Home, WhyUs, Suggestions, ContactInfo, Services, OurService, About, Team, Portfolio, Contact


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'


class WhyUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyUs
        fields = '__all__'


class SuggestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestions
        fields = '__all__'


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class OurServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurService
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
