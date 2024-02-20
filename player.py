from abc import ABC, abstractmethod


class Player():
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item: str):
        self.items.append(item)

    def print_items(self):
        for item in self.items:
            print(item)

    def check_items(self, item: str):
        if item in self.items:
            return True
        else:
            return False


player1 = Player(name="")


def name_player(name: str):
    player1.name = name
