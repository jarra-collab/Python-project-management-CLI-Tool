class Project:
    def __init__(self, title, description, tasks=None):
        self.title = title
        self.description = description
        self.tasks = tasks if tasks else []

    def add_task(self, task_obj):
        self.tasks.append(task_obj)

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "tasks": [t.to_dict() for t in self.tasks]
        }