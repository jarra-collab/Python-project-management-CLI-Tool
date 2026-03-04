import argparse
from apps.project import Project
from apps.tasks import Task
from apps.user import User
from apps.storage import Storage
from rich.console import Console
from rich.table import Table

console = Console()
db = Storage("data/database.json")

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI")
    subparsers = parser.add_subparsers(dest="command")

    user_parser = subparsers.add_parser("add-user")
    user_parser.add_argument("--name", required=True)
    user_parser.add_argument("--email", required=True)

    proj_parser = subparsers.add_parser("add-project")
    proj_parser.add_argument("--user", required=True)
    proj_parser.add_argument("--title", required=True)

    subparsers.add_parser("list")

    args = parser.parse_args()
    
    users = db.load_all()

    if args.command == "add-user":
        new_user = User(name=args.name, email=args.email)
        users.append(new_user)
        db.save_all(users)
        console.print(f"[green]Success:[/green] User {args.name} created.")

    elif args.command == "add-project":
        found_user = None
        for u in users:
            if u.name.lower() == args.user.lower():
                found_user = u
                break
        
        if found_user:
            new_proj = Project(title=args.title, description="No description provided")
            found_user.projects.append(new_proj)
            db.save_all(users)
            console.print(f"[blue]Project '{args.title}' added to {found_user.name}.[/blue]")
        else:
            console.print(f"[red]Error:[/red] User '{args.user}' not found.")

    elif args.command == "list":
        table = Table(title="Team Project Tracker")
        table.add_column("User", style="cyan", no_wrap=True)
        table.add_column("Email", style="white")
        table.add_column("Projects", style="magenta")

        for u in users:
            proj_names = ", ".join([p.title for p in u.projects]) if u.projects else "None"
            table.add_row(u.name, u.email, proj_names)
        
        console.print(table)

if __name__ == "__main__":
    main()