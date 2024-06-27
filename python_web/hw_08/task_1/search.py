from mongoengine import connect
from task_1.models import Author, Quote  # Import models here

connect(
    host="mongodb+srv://bnjgvcom63:upwv752i9kiojxcJ@cluster0.yzs2ekw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)


def search_quotes():
    while True:
        command = input("Enter command (or 'exit' to quit): ")

        if command.startswith("name:"):
            author_name = command[len("name:") :].strip()
            author = Author.objects(fullname=author_name).first()
            if author:
                quotes = Quote.objects(author=author)
                for quote in quotes:
                    print(quote.quote)
            else:
                print("Author not found.")

        elif command.startswith("tag:"):
            tag = command[len("tag:") :].strip()
            quotes = Quote.objects(tags=tag)
            for quote in quotes:
                print(quote.quote)

        elif command.startswith("tags:"):
            tags = command[len("tags:") :].strip().split(",")
            quotes = Quote.objects(tags__in=tags)
            for quote in quotes:
                print(quote.quote)

        elif command == "exit":
            break

        else:
            print("Invalid command.")


if __name__ == "__main__":
    search_quotes()
