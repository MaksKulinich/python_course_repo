import json
import pika
from mongoengine import connect
from model import Contact
import time

connect(
    host="mongodb+srv://bnjgvcom63:upwv752i9kiojxcJ@cluster0.yzs2ekw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)


rabbitmq_host = "localhost"
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()
channel.queue_declare(queue="email_queue")


def send_email(contact):
    print(f"Sending email to {contact.email}")

    time.sleep(2)
    print(f"Email sent to {contact.email}")


def callback(ch, method, properties, body):
    data = json.loads(body)
    contact_id = data["id"]
    contact = Contact.objects(id=contact_id).first()
    if contact:
        send_email(contact)
        contact.message_sent = True
        contact.save()
        print(f"Updated contact {contact.fullname} status to sent")


channel.basic_consume(queue="email_queue", on_message_callback=callback, auto_ack=True)

print("Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
