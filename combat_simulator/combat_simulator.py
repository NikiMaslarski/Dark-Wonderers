import os
import sys
os.chdir('../player')
sys.path.append(os.getcwd())
os.chdir('../units')

from player import Player
from units import ALL_RACE_UNITS




def fight(damage1, health1, damage2, health2):
    """
    Returns tuple(winning player, damage takenfrom the winner) 
    """

    outcome1 = damage1 - health2
    outcome2 = damage2 - health1

    if outcome1 > outcome2:
        return (1, outcome1)
    elif outcome1 < outcome2:
        return(2, outcome2)


def get_total_damage(army, race):
    damage = 0
    units = [unit_name for unit_name in ALL_RACE_UNITS[race]]
    for i in range(0, 4):
        damage += army[i] * ALL_RACE_UNITS[race][units[i]].damage
    return damage


def get_health(army, race):
    health = 0
    units = [unit_name for unit_name in ALL_RACE_UNITS[race]]
    for i in range(0, 4):
        health += army[i] * ALL_RACE_UNITS[race][units[i]].health
    return health


def hero_combat(player1, player2):
    """ Manages deaths and returns the winner name """
    damage1 = get_total_damage(player1.hero.army, player1.race)
    health1 = get_health(player1.hero.army, player1.race)
    damage2 = get_total_damage(player2.hero.army, player2.race)
    health2 = get_health(player2.hero.army, player2.race)

    winner = fight(damage1, health1, damage2, health2)

    if winner[0] == 1:
        player1.hero.gain_experience(winner[1] / -100)
        player2.hero = None
        return player1.name
    elif winner[0] == 2:
        player2.hero.gain_experience(winner[1] / -100)
        player1.hero = None
        return player2.name

