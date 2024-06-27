from task_1.models import Author, Quote
from mongoengine import connect
import json


connect(
    host="mongodb+srv://bnjgvcom63:upwv752i9kiojxcJ@cluster0.yzs2ekw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

with open("authors.json", "r", encoding="utf-8") as authors_file:
    authors_data = json.load(authors_file)
    for author in authors_data:
        autors = Author(
            fullname=author["fullname"],
            born_date=author["born_date"],
            born_location=author["born_location"],
            description=author["description"],
        )
        autors.save()


with open("qoutes.json", "r", encoding="utf-8") as qoutes_file:
    quotes_data = json.load(qoutes_file)
    for quote in quotes_data:
        author_name = quote["author"]
        author = Author.objects(fullname=author_name).first()
        if author:
            quote = Quote(tags=quote["tags"], author=author, quote=quote["quote"])
            quote.save()
