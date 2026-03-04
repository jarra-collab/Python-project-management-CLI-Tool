import json
import os
from apps.user import User
from apps.project import Project
from apps.tasks import Task

class Storage:
    def __init__(self, file_path="database.json"):
        self.file_path = file_path
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def save_all(self, users):
        try:
            with open(self.file_path, "w") as f:
                json_data = [u.to_dict() for u in users]
                json.dump(json_data, f, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def load_all(self):
        if not os.path.exists(self.file_path):
            return []

        try:
            with open(self.file_path, "r") as f:
                raw_data = json.load(f)
                
                users = []
                for u_dict in raw_data:
                    new_user = User(u_dict['name'], u_dict['email'])
                    
                    for p_dict in u_dict.get('projects', []):
                        new_project = Project(p_dict['title'], p_dict['description'])
                        for t_dict in p_dict.get('tasks', []):
                            new_task = Task(t_dict['title'], t_dict['assigned_to'], t_dict['status'])
                            new_project.add_task(new_task)
                        new_user.projects.append(new_project)
                    
                    users.append(new_user)
                return users
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error loading data: {e}")
            return []