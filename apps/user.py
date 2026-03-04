class User:
    def __init__(self, name, email, projects=None):
        self.name = name
        self.email = email
        self.projects = projects if projects else []

    def to_dict(self):
        return {
            "name": self.name, 
            "email": self.email, 
            "projects": [p.to_dict() for p in self.projects]
        }