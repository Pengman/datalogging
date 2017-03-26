from peewee import *

db = SqliteDatabase('data.db')

class Konto(Model):
    navn = CharField()
    bankId = IntegerField()

    class Meta:
        database = db # This model uses the "people.db" database.

class KontoLinie(Model):
    tekst = CharField()
    dato = DateField()
    beloeb_oerer = IntegerField()
    import_dato = DateField()
    konto = ForeignKeyField(Konto, related_name = 'transaktioner')

    class Meta:
        database = db # This model uses the "people.db" database.

class Tag(Model):
    tekst = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.


class Tagget_Beloeb(Model):
    beloeb_oerer = IntegerField()
    tag = ForeignKeyField(Tag, related_name = 'beloeb')
    linie = ForeignKeyField(KontoLinie, related_name='tags')

    class Meta:
        database = db # This model uses the "people.db" database.
