from mongoengine import Document, IntField, StringField, ReferenceField # :id phu

class Vote(Document):
    name = StringField()
    choice = StringField()
    #vote = IntField()
    poll = ReferenceField("Poll")