from random import randint, random
from classes.pet import Shiba

class Ninja:

    def __init__( self , name, pet_name ):
        self.name = name
        self.agility = 10
        self.speed = 5
        self.health = 100
        self.evasion = 2
        self.pet = Shiba(pet_name)
    
    def show_stats( self ):
        print(f"---Current Stats---")
        print(f"Name: {self.name}\nAgility: {self.agility}\nSpeed: {self.speed}\nHealth: {self.health}\nPet: = {self.pet.make_self_known().name}\n")

    def turn(self,pirate):
        roll = randint(1,6)
        if  roll <= 5 :
            self.attack(pirate)
        elif roll == 3:
            print(f"{self.name} tripped and skipped their turn!\n")
        else:
            self.shiba_bite(pirate)
        return self
            

    def attack( self , pirate ):
        pirate.health -= (self.agility * 1.5)
        print(f"{pirate.name} was slashed!")
        pirate.debuff().show_stats()
        return self

    def check_evade (self):
        if self.evasion > randint(1,6):
            return True
        else:
            return False

    def shiba_bite(self, pirate):
        if self.pet.health > 0:
            pirate.health -= self.pet.attack
            self.pet.health -= randint(19,31)
            print(f"{self.pet.name} took a bite of {pirate.name} they have {pirate.health} remaining.\n")
        else:
            print(f"{self.pet.name} has already fainted!\n")
