from django.db import models


# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Home(TimeStamp):
    title = models.CharField(max_length=212)
    content = models.TextField()
    image = models.ImageField(upload_to='home/')

    def __str__(self):
        return self.title


class WhyUs(TimeStamp):
    image = models.ImageField(upload_to='why/')
    description = models.TextField()


class Services(TimeStamp):
    service_name = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='service/')


class Suggestions(TimeStamp):
    price = models.CharField(max_length=212)
    icon_started = models.BooleanField(default=False)
    feature = models.CharField(max_length=212)


class Team(TimeStamp):
    name = models.CharField(max_length=212)
    surname = models.CharField(max_length=212)
    profession = models.CharField(max_length=212)
    image = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name


class About(TimeStamp):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(max_length=212)

    def __str__(self):
        return self.title


class OurService(TimeStamp):
    title = models.CharField(max_length=212)
    description = models.TextField()
    icon_now = models.BooleanField(default=False)
    image = models.ImageField(upload_to='service/')
    title2 = models.CharField(max_length=212)
    description2 = models.TextField()

    def __str__(self):
        return self.title


class Portfolio(TimeStamp):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return self.title


class Contact(TimeStamp):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name


class ContactInfo(TimeStamp):
    phone = models.CharField(max_length=212)
    email = models.EmailField()
