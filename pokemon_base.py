from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
from random_gen import RandomGen
from array_sorted_list import *

""" 
Implement the groundwork of Pokemon.
"""
__author__ = "Scaffold by Jackson Goerner, Code by Chai Wai Jin, Hang Jui Kai & Jeremy To Jun Wei"


class PokemonBase(ABC):
    """ Implements abstract method for each of the pokemon classes"""

    def __init__(self, poke_type: PokeType, poke_name: str, level: int) -> None:
        """ Initialisation

            :param arg1: type of pokemon
            :param arg2: name of pokemon
            :param arg3: level of pokemon
            :raises ValueError: when the argument does not meet the condition
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does initialize all the attributes.
        """
        if not isinstance(poke_type, PokeType):
            raise ValueError("Pokemon Type is invalid")
        if not isinstance(poke_name, str) or len(poke_name) <= 0:
            raise ValueError("Pokemon name must have length > 0")
        if not isinstance(level, int) or level <= 0:
            raise ValueError("Level must be positive integer")

        self.poke_type = poke_type
        self.poke_name = poke_name
        self.level = level
        self.status = "free"

    def is_fainted(self) -> bool:
        """ To indicate that Pokemon is fainted.
        
            :complexity: Best/Worst O(1), since every operation is constant time
        
            The function returns True if the hp of Pokemon is less than or equal to 0, otherwise
            returns False if its hp greater than 0.
        """
        return self.hp <= 0

    def level_up(self) -> None:
        """ Pokemon acquire 1 level.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.
            
            The function increases the level of Pokemon by 1.
        """
        self.level += 1

    def get_poke_type(self) -> PokeType:
        """ To get the type of Pokemon.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.
            
            The function returns type of Pokemon.
        """
        return self.poke_type

    def get_hp(self) -> int:
        """ To get the hp of the Pokemon.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.
            
            The function returns the hp of Pokemon.
        """
        return self.hp
    
    def set_hp(self, hp: int) -> None:
        """ To set the hp of Pokemon.

            :param arg1: hit points of pokemon
            :complexity: Best/Worst O(1), since all intrusctions are constant.
            
            The function reassigns the new hit points of Pokemon.
        """
        self.hp = hp

    def get_speed(self) -> int:
        """ To get the speed points of Pokemon.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.
            
            The function returns the speed points of Pokemon.
        """
        return self.speed

    def set_speed(self, speed: int) -> None:
        """ To set the speed of Pokemon.
        
            :param arg1: speed points of pokemon
            :complexity: Best/Worst O(1), since all intrusctions are constant.
            
            The function reassigns the speed points of Pokemon.
        """
        self.speed = speed

    def get_attack_damage(self) -> int:
        """ To get the attack points of Pokemon.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.
            
            The function returns the attack points of Pokemon.
        """
        return self.attack_damage

    def set_attack_damage(self, attack: int) -> None:
        """ To set the attack damage to a Pokemon.
        
            :param arg1: attack points of pokemon
            :complexity: Best/Worst O(1), since all intrusctions are constant.
            
            The function reassigns the attack points of Pokemon.
        """
        self.attack_damage = attack

    def get_defence(self) -> int:
        """ To get the defence points of Pokemon. 
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.
        
            The function returns the defence points of Pokemon.
        """
        return self.defence

    def get_level(self) -> int:
        """ To get the level of Pokemon.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.
            
            The function returns the level of Pokemon.
        """
        return self.level

    def get_status(self) -> str:
        """ To get the status of Pokemon. 
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.
            
            The function returns the status of Pokemon.
        """
        return self.status
    
    def set_status(self, status: str | None) -> None:
        """ To set the status of Pokemon.
        
            :param arg1: status of pokemon
            :complexity: Best/Worst O(1), since all intrusctions are constant.
            
            The function reassigns the status of Pokemon.
        """
        self.status = status
    
    def get_max_hp(self) -> int:
        """ To get the max hp of Pokemon.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.
            
            The function returns the max hp of Pokemon.
        """
        return self.max_hp

    def lose_hp(self, lost_hp: int) -> None:
        """ Pokemon lose hp. 

            :param arg1: effective attack points
            :complexity: Best/Worst O(1), since all intrusctions are constant.
        
            The function decreases the hp of Pokemon by lost_hp parameter.
        """
        self.hp -= lost_hp

    def heal(self) -> None:
        """ Pokemon heal.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.
            
            The function reassigns the hp of Pokemon to its max hp and status to None.
        """
        self.hp = self.get_max_hp()
        self.status = "free"

    @abstractmethod
    def defend(self, damage: int) -> None:
        """ To calculate how the Pokemon reacts when being attacked with effective attack points.

            :param arg1: effective attack points
            :complexity: Best/Worst O(1), since all intrusctions are constant.
        """
        pass

    def calculate_damage(self, other: PokemonBase) -> float:
        """ To calculate the damage of Pokemon.

            :param arg1: opposing pokemon
            :complexity: Best/Worst O(1), since all intrusctions are constant.
            
            The function determine the multiplier applied to the attacking stat.
        """
        attack_stat = [[1, 2, 0.5, 1, 1],
                       [0.5, 1, 2, 1, 1],
                       [2, 0.5, 1, 1, 1],
                       [1.25, 1.25, 1.25, 2, 0],
                       [1.25, 1.25, 1.25, 0, 1]]

        damage = self.get_attack_damage() * attack_stat[self.get_poke_type().value][other.get_poke_type().value]
        return damage

    def attack(self, other: PokemonBase) -> None:
        """ One Pokemon attacking another.
                
            :param arg1: opposing pokemon
            :complexity: Best/Worst O(1), everything is constant time
            
            The function determines the status effects on attack damage/ redirecting attacks of Pokemon, proceed with the
            attack, Pokemon lose hp accordingly.
        """
        # Step 1: Status effects on attack damage / redirecting attacks
        # Step 2: Do the attack
        # Step 3: Losing hp to status effects
        # Step 4: Possibly applying status effects
        
        # to determine the status of Pokemon
        if self.get_status() != "sleep":
            if self.get_status() == "free" or self.get_status() == "paralysis":
                damage = self.calculate_damage(other)
                other.defend(int(damage))
            elif self.get_status() == "confuse":
                is_confuse = RandomGen.random_chance(0.5)
                if is_confuse:
                    damage = self.calculate_damage(self)
                    self.defend(int(damage))
                else:
                    damage = self.calculate_damage(other)
                    other.defend(int(damage))
            elif self.get_status() == "burn":
                damage = self.calculate_damage(other) / 2
                other.defend(int(damage))
                self.lose_hp(1)
            elif self.get_status() == "poison":
                damage = self.calculate_damage(other)
                other.defend(int(damage))
                self.lose_hp(3)

            status_list = ["burn", "poison", "paralysis", "sleep", "confuse"]

            # to determine whether Pokemon inflicts status on another Pokemon
            status_inflict = RandomGen.random_chance(0.2)
            if status_inflict:
                other.status = status_list[self.get_poke_type().value]

    def get_poke_name(self) -> str:
        """ To get the name of Pokemon.

            :complexity: Best/Worst O(1), since all intrusctions are constant.
            
            The function return the name of Pokemon.
        """
        return self.poke_name

    def __str__(self) -> str:
        """ Magic method constructing a string representation of Pokemon object. 
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.
        """
        return f'LV. {self.get_level()} {self.get_poke_name()}: {self.get_hp()} HP'

    @abstractmethod
    def should_evolve(self) -> bool:
        """ To indicate that the Pokemon should evolve.
                
            The function returns True if Pokemon should evolve, else returns False.
        """
        pass

    @abstractmethod
    def can_evolve(self) -> bool:
        """ To indicate that the Pokemon can evolve.
                
            The function returns True if Pokemon can evolve, else returns False.
        """
        pass

    @abstractmethod
    def get_evolved_version(self) -> PokemonBase:
        """ Get the evolved version of the pokemon.
        
            :raise ValueError: if Pokemon not able to evolve

            The function returns the evolved version of Pokemon if pokemon can evolve, else raises a ValueError.
        """
        pass

class PokeType(Enum):
    """ Used to select the proper Pokemon type and keep the listings together.
    """
    FIRE = 0
    GRASS = 1
    WATER = 2
    GHOST = 3
    NORMAL = 4