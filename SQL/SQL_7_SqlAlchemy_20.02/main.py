from sqlalchemy import or_
from db.models import User, Profile, Task
from db import Session


def main():
    session=Session()
    try:
        while user_input := input():
            args = user_input.split()
            match args[0]:
                case "create-user" | "cr-u":
                    name = args[1]
                    email = args[2]
                    new = User(username=name, email=email)
                    session.add(new)
                    session.commit()

                case "create-profile" | "cr-pf":
                    new = Profile(bio=args[1], phone=args[2], user_id=args[3])
                    session.add(new)
                    session.commit()

                case "create-project" | "cr-pj":
                    new = User(title=args[1], description=args[2], task=args[3])
                    session.add(new)
                    session.commit()

                case "create-task" | "cr-t":
                    new = User(title=args[1], status=args[2], project_id=args[3])
                    session.add(new)
                    session.commit()

                case "all" | "a":
                    tasks = session.query(Task).all()
                    print(f"Found {len(tasks)} task(s)")
                    for task in tasks:
                        print(
                            f"name: {task.name}, description: '{task.description}', completed: {task.completed}"
                        )
                case "find-u" | "search-u" | "f-u" | "s-u":
                    pattern = " ".join(args[1:])
                    fs = session.query(User).filter(or_(User.name.contains(pattern), User.description.contains(pattern))).all()
                    print(f"Found {len(fs)} line(s)")
                    for f in fs:
                        print(
                            f"id: {f.id}, username: {f.name}, description: '{f.description}', completed: {f.completed}"
                        )

                case "complete" | "co" | "c":
                    ids = int(args[1])
                    task = session.query(Task).filter_by(id=ids).one()
                    task.completed = True
                    session.commit()

                case "delete" | "d":
                    ids = int(args[1])
                    task = Task.get(ids)
                    session.delete(task)
                    session.commit()

                case "quit" | "q" | "exit":
                    break

                case _:
                    raise ValueError("invalid command-line argument")

    except EOFError:
        pass


if __name__ == "__main__":
    main()