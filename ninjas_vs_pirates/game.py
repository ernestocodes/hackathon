from random import randint
from classes.ninja import Ninja
from classes.pirate import Pirate
from classes.pet import Parrot

def fight(ninja,pirate):
    print ("----FIGHT!----")
    turn = 1
    while ninja.health > 0 and pirate.health > 0:
        if randint(1,6)%2 == 0: 
            print(f"--Turn{turn}--")
            ninja.turn(pirate)
            turn += 1
        else: 
            print(f"--Turn{turn}--")
            pirate.turn(ninja)
            turn += 1
    if ninja.health > 0:
        return ninja
    return pirate


def declare_winner(winner):
    print(f"\n ***{winner.name} wins!***")

terry = Ninja("Terry", "Bolt")
erica = Pirate("Erica", "Percy")
fighter = fight(terry,erica)
declare_winner(fighter)