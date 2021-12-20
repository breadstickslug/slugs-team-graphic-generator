from django.db import models

# Create your models here.

class Move(models.Model):
    move_id = models.IntegerField(default=1, unique=True)
    move_name = models.CharField(max_length=200, default="")
    move_type_id = models.IntegerField(default=1)
    move_base_power = models.IntegerField(default=0)
    move_pp = models.IntegerField(default=1)
    move_priority = models.IntegerField(default=0)
    move_accuracy = models.IntegerField(default=100)
    move_damage_class = models.IntegerField(default=1)
    move_description = models.CharField(max_length=500)
    hidden = models.BooleanField(default=False)
    def __str__(self):
        return self.move_name
    

class Species(models.Model):
    species_id = models.IntegerField(default=1)
    species_name = models.CharField(max_length=100)
    species_form_name = models.CharField(max_length=100, blank=True)
    species_type_1 = models.IntegerField(default=1)
    species_type_2 = models.IntegerField(default=1, null=True)
    species_ability_1 = models.IntegerField(default=1)
    species_ability_2 = models.IntegerField(default=1, null=True)
    species_ability_3 = models.IntegerField(default=1, null=True)
    species_gender_ratio = models.IntegerField(default=1)
    learnset = models.ManyToManyField(Move)
    hidden = models.BooleanField(default=False)
    def __str__(self):
        return self.species_name

class Item(models.Model):
    item_id = models.IntegerField(default=1, unique=True)
    item_name = models.CharField(max_length=100, default="")
    item_description = models.CharField(max_length=500)
    hidden = models.BooleanField(default=False)
    def __str__(self):
        return self.item_name

class Ability(models.Model):
    ability_id = models.IntegerField(default=1, unique=True)
    ability_name = models.CharField(max_length=100, default="")
    hidden = models.BooleanField(default=False)
    def __str__(self):
        return self.ability_name

class TeamMon(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERLESS = 'X'
    GENDER_CHOICES = [(MALE, 'Male'), (FEMALE, 'Female'), (GENDERLESS, 'Genderless')]
    species = models.ManyToManyField(Species)
    ability = models.IntegerField(default=1)
    held_item = models.ManyToManyField(Item)
    level = models.IntegerField(default=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    move_1 = models.ManyToManyField(Move, related_name='+')
    move_2 = models.ManyToManyField(Move, related_name='+')
    move_3 = models.ManyToManyField(Move, related_name='+')
    move_4 = models.ManyToManyField(Move, related_name='+')

class Team(models.Model):
    pos_1 = models.OneToOneField(TeamMon, on_delete=models.CASCADE, related_name='+')
    pos_2 = models.OneToOneField(TeamMon, on_delete=models.CASCADE, related_name='+')
    pos_3 = models.OneToOneField(TeamMon, on_delete=models.CASCADE, related_name='+')
    pos_4 = models.OneToOneField(TeamMon, on_delete=models.CASCADE, related_name='+')
    pos_5 = models.OneToOneField(TeamMon, on_delete=models.CASCADE, related_name='+')
    pos_6 = models.OneToOneField(TeamMon, on_delete=models.CASCADE, related_name='+')
    
