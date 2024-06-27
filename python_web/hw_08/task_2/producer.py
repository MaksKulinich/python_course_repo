import json
import pika
from faker import Faker
from mongoengine import connect
from model import Contact


connect(
    host="mongodb+srv://bnjgvcom63:upwv752i9kiojxcJ@cluster0.yzs2ekw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)


rabbitmq_host = "localhost"
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()
channel.queue_declare(queue="email_queue")


fake = Faker()
contacts = []
for _ in range(10):
    contact = Contact(fullname=fake.name(), email=fake.email())
    contact.save()
    contacts.append(contact)


for contact in contacts:
    message = json.dumps({"id": str(contact.id)})
    channel.basic_publish(exchange="", routing_key="email_queue", body=message)
    print(f"Sent contact {contact.fullname} to the queue")

connection.close()
