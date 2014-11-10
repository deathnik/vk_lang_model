from django.db import models

INDEX_FIELD_LENGTH = 255


class Person(models.Model):
    vk_id = models.CharField(db_index=True, max_length=INDEX_FIELD_LENGTH)
    firstName = models.CharField(db_index=True, max_length=INDEX_FIELD_LENGTH)
    lastName = models.CharField(db_index=True, max_length=INDEX_FIELD_LENGTH)
    #json
    otherInformation = models.TextField()


class Conversation(models.Model):
    first = models.ForeignKey(Person, related_name='first')
    second = models.ForeignKey(Person, related_name='second')
    #zipped
    data = models.TextField()


class GroupConversation(models.Model):
    group = models.CharField(db_index=True, max_length=INDEX_FIELD_LENGTH)
    #zipped
    data = models.TextField()


class GroupConversationMapping(models.Model):
    group = models.ForeignKey(GroupConversation)
    person = models.ForeignKey(Person)


class PersonLangModel(models.Model):
    person = models.ForeignKey(Person)
    #zipped pickled object
    data = models.TextField()