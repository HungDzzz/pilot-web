from mongoengine import Document, StringField, ListField

class Poll (Document):
    question = StringField()
    options = ListField(StringField())
    code = StringField()