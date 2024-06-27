from mongoengine import Document
from mongoengine.fields import (
    StringField,
    EmailField,
    BooleanField,
)


class Contact(Document):
    fullname = StringField()
    email = EmailField()
    send_message = BooleanField(default=False)
