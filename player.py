from abc import ABC, abstractmethod

class Player():
    def __init__(self, name):
        self.name = name
        self.items = []
        self.skills = {}

    def pickup_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)

    def use_item(self, item):
        item.use()

    def add_skill(self, skill):
        self.skills.append(skill)

    def remove_skill(self, skill):
        self.skills.remove(skill)

    def print_items(self):
        for item in self.items:
            print(f"{item.name}: {item.description}")

    def print_skills(self):
        for skill in self.skills:
            print(f"{skill.name}: {skill.description}")

class Skill(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def use(self):
        pass


