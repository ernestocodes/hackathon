

class Parrot:
    def __init__(self, name):
        self.name = name
        self.attack = 30
        self.health = 30

    # def attack(self, ninja):
    #     while self.health > 0:
    #         ninja.health -= self.

    def make_self_known(self):
        if self.health > 0:
            print(f"{self.name} want a cracker!")
        else:
            print(f"{self.name} is recovering.")
        return self

class Shiba:
    def __init__(self, name):
        self.name = name
        self.attack = 10
        self.health = 60
    
    def make_self_known(self):
        if self.health > 0:
            print(f"{self.name} woofs!")
        else:
            print(f"{self.name} is recovering.")
        return self
