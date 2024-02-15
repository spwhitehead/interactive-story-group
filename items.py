from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def use(self):
        pass

class Key(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def use(self):
        print(f"You use your {self.name} to open the door.")

