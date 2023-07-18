from django.db import models

# Create your models here.
size_choie = (
    ('Tiny','Tiny'),
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
)

friendliness_choice = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5)
)
trainability_choice = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5)
)
shedding_choice = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5)
)
exerciseneeds_choice = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5)
)
gender_choice = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)
class Breed (models.Model):
    name = models.CharField(max_length=20)
    size = models.CharField(max_length=10, choices = size_choie)
    friendliness = models.IntegerField(choices=friendliness_choice)
    trainability = models.IntegerField(choices=trainability_choice)
    sheddingamount = models.IntegerField(choices=shedding_choice)
    exerciseneeds = models.IntegerField(choices=exerciseneeds_choice)

    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField();
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=gender_choice)
    color = models.CharField(max_length=10)
    favouritefood = models.CharField(max_length=10)
    favouritetoy = models.CharField(max_length=10)

    def __str__(self):
        return self.name
