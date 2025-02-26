"""
main part
"""
from db.models import Book, Visitor, Status


def main():
    """
    main function
    """
    db_path = "./library.db"
    book_table = Book(db_path)
    status_table = Status(db_path)
    visitor_table = Visitor(db_path)

    try:
        while user_input := input():
            args = user_input.split()
            match args[0]:
                case "create-book" | "cr-b":
                    book_table.objects.create(args[1], args[2], args[3], args[4], args[5], args[6])

                case "create-visitor" | "cr-v":
                    visitor_table.objects.create(args[1], args[2], args[3], args[4], args[5])

                case "create-status" | "cr-s":
                    status_table.objects.create(args[1], args[2])

                case "all-book" | "a-b":
                    a = book_table.objects.all()
                    for i in a:
                        print(f"name: {i[0]}, author: {i[1]}, year: {i[2]}, \
                              edition: {i[3]}, bookcase_id: {i[4]}, bookshelf_id: {i[5]}")

                case "all-visitor" | "a-v":
                    a = visitor_table.objects.all()
                    for i in a:
                        print(f"name: {i[0]}, surname: {i[1]}, middle_name: {i[2]}, \
                              library_card_id: {i[3]}, adress: {i[4]}")

                case "all-status" | "a-s":
                    a = status_table.objects.all()
                    print(f"Found {len(a)} lines")
                    for i in a:
                        print(f"book_id: {i[0]}, 'visitor_id: {i[1]}")

                case "delete-book" | "d-b":
                    ids = int(args[1])
                    book_table.objects.delete(ids)

                case "delete-visitor" | "d-v":
                    ids = int(args[1])
                    visitor_table.objects.delete(ids)

                case "delete-status" | "d-s":
                    ids = int(args[1])
                    status_table.objects.delete(ids)

                case "get-place" | "get-bp":
                    name = book_table.objects.get_place(args[1], args[2])
                    print(f"The book is {name}")

                case "get-author" | "get-ba":
                    print(f"{args[1]} wrote {book_table.objects.get_author(args[1])}")

                case "get-year" | "get-by":
                    print(f"In {args[1]} published: {book_table.objects.get_year(args[1])[0]}")

                case "get_visitor" | "get-sv":
                    z = status_table.objects.get_visit(args[1])
                    print(f"The owner of {args[1]} is {z[0]} and its library card id is {z[1]}")

                case "get_books" | "get-sb":
                    print(f"The visitor {args[1]} owns {status_table.objects.get_books(args[1])}")

                case "quit" | "q" | "exit":
                    break

                case _:
                    raise ValueError("invalid command-line argument")

    except EOFError:
        pass


if __name__ == "__main__":
    main()
