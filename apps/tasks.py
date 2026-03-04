class Task:
    def __init__(self, title, assigned_to, status="In Progress"):
        self.title = title
        self.assigned_to = assigned_to
        self.status = status

    def to_dict(self):
        return {"title": self.title, "assigned_to": self.assigned_to, "status": self.status}



