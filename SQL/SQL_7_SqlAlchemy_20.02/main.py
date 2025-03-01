"""
main
"""

from db.models import User, Profile, Task, Project
from db import Session


def main():
    """
    The main
    """
    session=Session()
    try:
        while user_input := input():
            args = user_input.split()
            match args[0]:
                case "create-user" | "cr-u":
                    name = args[1]
                    email = args[2]
                    new = User(name, email)
                    session.add(new)
                    session.commit()

                case "create-profile" | "cr-pf":
                    user = session.query(User).filter_by(id=args[3]).first()
                    if user: # Создаю только если юзер существует
                        new = Profile(args[1], args[2], args[3])
                        session.add(new)
                        session.commit()
                    else:
                        print('Please create a user first.')

                case "create-project" | "cr-pj":

                    new = Project(args[1], args[2])
                    session.add(new)
                    session.commit()

                case "create-task" | "cr-t":
                    project = session.query(Project).filter_by(id=args[3]).first()
                    if project:
                        new = Task(args[1], args[2], args[3])
                        session.add(new)
                        session.commit()
                    else:
                        print('Please create a project first.')

                case "all-u" | "a-u":
                    findings = session.query(User).all()
                    print(f"Found {len(findings)} user(s)")
                    for f in findings:
                        print(
                            f"username: {f.username}, email: '{f.email}'"
                        )

                case "all-pf" | "a-pf":
                    findings = session.query(Profile).all()
                    print(f"Found {len(findings)} profile(s)")
                    for f in findings:
                        print(
                            f"bio: {f.bio}, phone: '{f.phone}', user_id: {f.user_id}"
                        )

                case "all-pj" | "a-pj":
                    findings = session.query(Project).all()
                    print(f"Found {len(findings)} project(s)")
                    for f in findings:
                        print(
                            f"title: {f.title}, description: '{f.description}'"
                        )

                case "all-t" | "a-t":
                    findings = session.query(Task).all()
                    print(f"Found {len(findings)} task(s)")
                    for f in findings:
                        print(
                            f"title: {f.title}, status: '{f.status}', project_id: {f.project_id}"
                        )

                case "edit-email" | "e-e":
                    username = args[1]
                    new_email = args[2]
                    new = session.query(User).filter_by(username).first()
                    if new:
                        new.email = new_email
                        session.commit()
                        print("Email updated")
                    else:
                        print("User not found.")

                case "edit-desc" | "e-desc":
                    title = args[1]
                    new_desc = args[2]
                    new = session.query(User).filter_by(title=title).first()
                    if new:
                        new.description = new_desc
                        session.commit()
                        print("Project description updated")
                    else:
                        print("Project not found.")

                case "edit-status" | "e-stat":
                    title = args[1]
                    new_stat = args[2]
                    new = session.query(User).filter_by(title=title).first()
                    if new:
                        new.status = new_stat
                        session.commit()
                        print("Status updated")
                    else:
                        print("Task not found.")

                case "delete-u" | "d-u":
                    ids = int(args[1])
                    new = session.query(User).filter_by(id=ids).first()
                    session.delete(new)
                    session.commit()
                    prf = session.query(Profile).filter_by(user_id=ids).first()
                    session.delete(prf)
                    session.commit()

                case "delete-pj" | "d-pj":
                    ids = int(args[1])
                    new = session.query(Project).filter_by(id=ids).first()
                    session.delete(new)
                    session.commit() # а то все ломается, перезапускаю сессию
                    session=Session()
                    tasks = session.query(Task).filter_by(project_id=ids)
                    for t in tasks:
                        session.delete(t)
                    session.commit()

                case "delete-pf" | "d-pf":
                    ids = int(args[1])
                    new = session.query(Profile).filter_by(id=ids).first()
                    session.delete(new)
                    session.commit()

                case "delete-t" | "d-t":
                    ids = int(args[1])
                    task = session.query(Task).filter_by(id=ids).first()
                    session.delete(task)
                    session.commit()

                # Типо демонстрация связей ниже
                case "find-user-pj":
                    pattern = args[1]
                    fs = session.query(User).filter(User.name.contains(pattern)).all()
                    print(f"Found {len(fs)} line(s). On which projects does user work")
                    for f in fs:
                        print(f"id: {f.id}, username: {f.name}, projects: {f.projects}")

                case "find-user-pf":
                    pattern = args[1]
                    fs = session.query(Profile).filter(Profile.user_id.contains(pattern)).all()
                    print(f"Found {len(fs)} line(s). Shows the user's profile")
                    for f in fs:
                        print(f"id: {f.id}, username: {f.user.username}," \
                            f"projects: {f.bio}, phone: {f.phone}")

                case "find-pj-t":
                    pattern = args[1]
                    fs = session.query(Project).filter(Project.title.contains(pattern)).all()
                    print(f"Found {len(fs)} line(s). All tasks of a project")
                    for f in fs:
                        print(f"id: {f.id}, title: {f.title}, tasks: {f.task}")

                case "quit" | "q" | "exit":
                    break

                case _:
                    raise ValueError("invalid command-line argument")

    except EOFError:
        pass


if __name__ == "__main__":
    main()
