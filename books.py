from mongoengine import IntField,document,StringField
class Books(document):
    ID =IntField(required=True)
    NAME = StringField(required=True)
