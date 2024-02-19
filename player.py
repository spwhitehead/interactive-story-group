from abc import ABC, abstractmethod

class Player():
    def __init__(self, name):
        self.name = name
        self.items = []
        self.skills = {}

    def add_item(self, item):
        self.items.append(item)

    def print_items(self):
        for item in self.items:
            print(f"{item.name}: {item.description}")
