# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Client(models.Model):
    nom = models.CharField(max_length=50, blank=True, null=True)
    prenom = models.CharField(max_length=50, blank=True, null=True)
    adresse = models.CharField(max_length=100, blank=True, null=True)
    statut = models.IntegerField()


class Service(models.Model):
    idservice = models.AutoField(db_column='idService', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=50, blank=True, null=True)
    adresse = models.CharField(max_length=50, blank=True, null=True)
    idclient = models.ForeignKey(Client, models.DO_NOTHING, db_column='idClient')  # Field name made lowercase.


class Typeabo(models.Model):
    refecence = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    idclient = models.ForeignKey(Client, models.DO_NOTHING, db_column='idClient')  # Field name made lowercase.

