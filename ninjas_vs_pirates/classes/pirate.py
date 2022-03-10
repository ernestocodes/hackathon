from random import randint
from classes.pet import Parrot 

class Pirate:

    def __init__( self , name, pet_name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.limb = 2
        self.pet = Parrot(pet_name)


    def show_stats( self ):
        print(f"---Current Stats---")
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nLimbs = {self.limb}\nPet: = {self.pet.make_self_known().name}\n")

    def turn(self,ninja):
        roll = randint(1,6)
        if  roll >= 5 :
            self.attack(ninja)
        elif roll >=2:
            self.potion()
        else:
            self.call_parrot(ninja)
        return self



    def attack( self , ninja ):
        if ninja.check_evade():
            print(f"{ninja.name} was too slick! The attack was evaded!")
            return self
        else:
            ninja.health -= self.strength * (.5 + (self.limb/4))
            print(f"{ninja.name} could not evade. Direct hit!")
            ninja.show_stats()
            return self

    def potion (self):
        self.health += 10
        print(f"{self.name} has used a potion and now has {self.health} health!\n")
        return self

    def call_parrot(self, ninja):
        if self.pet.health > 0:
            ninja.health -= self.pet.attack
            self.pet.health -= randint(15,31)
            print(f"{self.pet.name} pecked at {ninja.name} they have {ninja.health} remaining.\n")
        else:
            print(f"{self.pet.name} has already fainted!\n")
        return self

    def debuff (self):
        if randint(1,6) <4 and self.limb > 0:
            self.limb -= 1
        return self

