import datetime
from django.db import models
from django.utils import timezone
from geograpy.models import ZipCode
# Create your models here.
class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

'''class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    #first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30)
    fname = models.CharField(max_length=60, default=0)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default="S")


class Musician (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'Gold Silver Bronze')
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)

class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
class Manufacturer (models.Model):
    pass
class Car(models.Model):
    company_that_makes_it = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

class Topping(models.Model):
    pass

class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)

class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
class Article (models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline
'''

class Person(models.Model):
    name = models.CharField(max_length=128, default="k")

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128, default="k")
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    data_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)








