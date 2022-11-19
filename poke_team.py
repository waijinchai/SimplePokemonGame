from __future__ import annotations

"""
Generate PokeTeam which has a limit of 6 Pokemon, adds a battle mode and contains the classes for action and criterion
"""
__author__ = "Scaffold by Jackson Goerner, Code by Chai Wai Jin, Hang Jui Kai & Jeremy To Jun Wei"

from enum import Enum, auto
from pokemon_base import PokemonBase
from pokemon import *
from random_gen import RandomGen
from array_sorted_list import *
from stack_adt import ArrayStack
from queue_adt import CircularQueue
from linked_list import LinkedList

class Action(Enum):
    """
    Used to select the proper Pokemon action variable and keep the listings together. The number of enum members 
    starting from 1.
    """
    ATTACK = auto()
    SWAP = auto()
    HEAL = auto()
    SPECIAL = auto()
    
class Criterion(Enum):
    """
    Used to select the proper Pokemon criterion variable and keep the listings together. The number of enum members 
    starting from 1.
    """
    SPD = auto()
    HP = auto()
    LV = auto()
    DEF = auto()

class PokeTeam:
    """ Builds a PokeTeam with up to 6 pokemon and a battle mode."""
    
    POKEDEX = ["Charmander", "Charizard", "Bulbasaur", "Venusaur", "Squirtle", "Blastoise", "Gastly", "Haunter",
               "Gengar", "Eevee"]

    class AI(Enum):
        """
        Used to select the proper Pokemon AI variable and keep the listings together. The number of enum members 
        starting from 1.
        """
        ALWAYS_ATTACK = auto()
        SWAP_ON_SUPER_EFFECTIVE = auto()
        RANDOM = auto()
        USER_INPUT = auto()

    def __init__(self, team_name: str, team_numbers: list[int], battle_mode: int, ai_type: PokeTeam.AI, criterion=None, criterion_value=None) -> None:
        """ Initialises the instance variables of a PokeTeam object.

        :param args1: a string representing the name of the PokeTeam
        :param args2: a list of integers to indicate the team's respective numbers of each pokemon
        :param args3: an integer representing the battle mode
        :param args4: ai type of the PokeTeam
        :param args5: criterion of the PokeTeam

        :raises ValueError: if the arguments do not meet the pre-conditions set for it
        :complexity: best case O(max(team_numbers[idx])*n), worst case O(team_numbers[idx])n+(n*m)+n^2)
                     where n is the len(poke_team_lst) and m is the len(ret_adt)

        this method initialises all the attributes
        """

        if not isinstance(team_name, str) or len(team_name) <= 0:
            raise ValueError("Team name must be a string and the length must be > 0")
        if not isinstance(team_numbers, list) or len(team_numbers) != 5:
            raise ValueError("Team numbers must have 5 elements")
        if not isinstance(battle_mode, int) or battle_mode not in [0, 1, 2]:
            raise ValueError("Battle mode must be between 0 to 2 (inclusive)")
        if not isinstance(ai_type, PokeTeam.AI) or ai_type not in list(PokeTeam.AI):
            raise ValueError("ai type is invalid")
        if (isinstance(criterion, Criterion) and criterion not in list(Criterion)) or (not isinstance(criterion, Criterion) and criterion is not None):
            raise ValueError("criterion is not Valid")

        self.team_name = team_name
        self.team_numbers = team_numbers
        self.battle_mode = battle_mode
        self.ai_type = ai_type
        self.criterion = criterion
        self.criterion_value = criterion_value
        self.heal_count = 0
        poke_team_lst = self._generate_poke_team()
        self.poke_team_lst = self._battle_mode_adt(poke_team_lst)

    def get_heal_count(self) -> int:
        """ Returns the heal count
        :complexity: best/worst O(1)
        """
        return self.heal_count

    def reset_heal_count(self) -> None:
        """ Resets the heal count to zero
        :complexity: best/worst O(1)
        """
        self.heal_count = 0

    def increment_heal_count(self) -> None:
        """ increamenets the heal count by one
        :complexity: best/worst O(1)
        """
        self.heal_count += 1

    def get_team_name(self) -> str:
        """ Returns the team_name
        :complexity: best/worst O(1)
        """
        return self.team_name

    def get_team_numbers(self) -> list[int]:
        """ Returns the team numbers list
        :complexity: best/worst O(1)
        """
        return self.team_numbers

    def get_poke_team_lst(self) -> ArrayStack | CircularQueue | ArraySortedList:
        """ Returns the PokeTeam list
        :complexity: best/worst O(1)
        """
        return self.poke_team_lst
    
    @classmethod
    def random_team(cls, team_name: str, battle_mode: int, team_size=None, ai_mode=None, **kwargs) -> PokeTeam:
        """ Creates a random PokeTeam

        :param args1: a string representing the name of the PokeTeam
        :param args2: an integer representing the battle mode
        :param args3: an integer representing the team size
        :param args4: ai type of the PokeTeam

        :complexity: Best O(max(team_numbers[idx])*n) when it is battle_mode 0 or 1,
                     Worst O(max(team_numbers[idx])*n+(n*m)+n^2) when it is battle_mode 2,
                     where n is the len(poke_team_lst) and m is the len(ret_adt).

        This function creates a random team with the given arguments.
        If no team size is specified, a random one between 3 and 6 is chosen
        If no ai_mode is specified, it is set to Random as default
        """
        if team_size is None:
            team_size = RandomGen.randint(3, 6)

        team_size_lst = ArraySortedList(6)
        team_size_lst.add(ListItem(0, 0))
        team_size_lst.add(ListItem(0, team_size))
        for _ in range(4):
            team_size_lst.add(ListItem(0, RandomGen.randint(0, team_size)))

        team_numbers = []
        for idx in range(len(team_size_lst)-1):
            diff = team_size_lst[idx+1].key - team_size_lst[idx].key
            team_numbers.append(diff)

        if ai_mode is None:
            ai_mode = PokeTeam.AI.RANDOM

        poke_team = PokeTeam(team_name, team_numbers, battle_mode, ai_mode, **kwargs)

        return poke_team

    def _generate_poke_team(self) -> ArraySortedList:
        """ Determines how many Charmanders/Bulbasaurs/Squirtles/Gastlys/Eevees should be added to the team.
        
        :post: The list must have <= 6 elements 
        :complexity: Best/Worst O(max(team_numbers[idx])*n), where n is the len(poke_team_lst)

        """
        poke_team_lst = ArraySortedList(6)
        for idx in range(len(self.team_numbers)):
            if idx == 0:
                for _ in range(self.team_numbers[idx]):
                    poke_team_lst.add(ListItem(Charmander(), self.POKEDEX.index("Charmander")))
            elif idx == 1:
                for _ in range(self.team_numbers[idx]):
                    poke_team_lst.add(ListItem(Bulbasaur(), self.POKEDEX.index("Charizard")))
            elif idx == 2:
                for _ in range(self.team_numbers[idx]):
                    poke_team_lst.add(ListItem(Squirtle(), self.POKEDEX.index("Squirtle")))
            elif idx == 3:
                for _ in range(self.team_numbers[idx]):
                    poke_team_lst.add(ListItem(Gastly(), self.POKEDEX.index("Gastly")))
            elif idx == 4:
                for _ in range(self.team_numbers[idx]):
                    poke_team_lst.add(ListItem(Eevee(), self.POKEDEX.index("Eevee")))

        return poke_team_lst

    def _battle_mode_adt(self, poke_team_lst: ArraySortedList) -> ArrayStack | CircularQueue | ArraySortedList:
        """ Places the Pokemon in a Data Type depending on the battle mode.

        :param args: a list with <= 6 elements to represent the pokemon in the team
        :complexity: Best O(n) when it is battle_mode 0 or 1, worst case O((n*m)+n^2) when it is battle_mode 2,
                     where n is len(poke_team_lst) and m is len(ret_adt)
        """
        ret_adt = None
        if self.battle_mode == 0:
            ret_adt = ArrayStack(len(poke_team_lst))
            for idx in range(len(poke_team_lst)):
                ret_adt.push(poke_team_lst[len(poke_team_lst)-1-idx].value)
        elif self.battle_mode == 1:
            ret_adt = CircularQueue(len(poke_team_lst))
            for idx in range(len(poke_team_lst)):
                ret_adt.append(poke_team_lst[idx].value)
        elif self.battle_mode == 2:
            ret_adt = ArraySortedList(len(poke_team_lst))
            self.is_ascending = False
            ret_adt.add(ListItem(poke_team_lst[0].value, self._get_criterion_value(poke_team_lst[0].value)))
            for idx in range(1, len(poke_team_lst)):
                ret_adt.add(ListItem(poke_team_lst[idx].value, self._get_criterion_value(poke_team_lst[idx].value)))
                if self._get_criterion_value(ret_adt[idx].value) == self._get_criterion_value(ret_adt[idx-1].value):
                    if ret_adt[idx].key < ret_adt[idx-1].key:
                        ret_adt.delete_at_index(idx-1)
                        ret_adt.add(ListItem(poke_team_lst[idx].value, self._get_criterion_value(poke_team_lst[idx].value)))
                        ret_adt.add(ListItem(poke_team_lst[idx-1].value, self._get_criterion_value(poke_team_lst[idx-1].value)))
            ret_adt.insertion_sort_reverse_order()

        return ret_adt

    def _get_criterion_value(self, pokemon: PokemonBase) -> int | None:
        """ Returns the criterion value of a pokemon

        :param args: an instance of a pokemon class
        :complexity: O(1) since all operations are constant
        """
        if self.criterion is not None:
            val_lst = [pokemon.get_speed(), pokemon.get_hp(), pokemon.get_level(), pokemon.get_defence()]
            return val_lst[self.criterion.value-1]

    def return_pokemon(self, poke: PokemonBase) -> None:
        """ Returns a pokemon from on field to back into the team

        :param args: an instance of a pokemon class
        :complexity: Best O(1) when it is battle_mode 0 or 1, worst case O(n) when it is battle_mode 2,
                     where n is len(poke_team_lst)
        """
        if not poke.is_fainted():
            poke.set_status("free")
            if self.battle_mode == 0:
                self.poke_team_lst.push(poke)
            elif self.battle_mode == 1:
                self.poke_team_lst.append(poke)
            elif self.battle_mode == 2:
                if self.is_ascending:
                    self.poke_team_lst.add(ListItem(poke, self._get_criterion_value(poke)))
                else:
                    self.poke_team_lst.add_descending(ListItem(poke, self._get_criterion_value(poke)))

    def retrieve_pokemon(self) -> PokemonBase | None:
        """ Retrieve a pokemon from the PokeTeam

        :post: the poke_team_lst will lose an element(pokemon) if its not already empty
        :complexity: Best O(1) when it is battle_mode 0 or 1, Worst O(n) when it is battle_mode 2,
                     where n is the len(poke_team_lst)
        """
        if self.battle_mode == 0:
            return self.poke_team_lst.pop()
        elif self.battle_mode == 1:
            return self.poke_team_lst.serve()
        elif self.battle_mode == 2:
            return self.poke_team_lst.delete_at_index(0).value

    def special(self):
        """ Performs the special operation on the PokeTeam

        :post: the poke_team_lst will be shuffled depending on the battle mode
        :complexity: best case O(n), worst case O(n^2)
                     where n is len(poke_team_lst)

        this function swaps the first and last pokemon if it's battle mode 0
        swaps the first and second halves of the team if it's battle mode 1
        reverse the sorting order of the team if it's battle mode 2
        """
        if self.battle_mode == 0:
            temp_list = LinkedList()
            for idx in range(len(self.poke_team_lst)):
                temp_list.insert(idx, self.poke_team_lst.pop())
            temp = temp_list[0]
            temp_list[0] = temp_list[len(temp_list)-1]
            temp_list[len(temp_list)-1] = temp
            for idx in range(len(temp_list)):
                self.poke_team_lst.push(temp_list[len(temp_list)-1-idx])
        elif self.battle_mode == 1:
            temp_stack = ArrayStack(len(self.poke_team_lst)//2)
            for _ in range(len(self.poke_team_lst)//2):
                pokemon = self.poke_team_lst.serve()
                temp_stack.push(pokemon)
            for _ in range(len(temp_stack)):
                self.poke_team_lst.append(temp_stack.pop())
        elif self.battle_mode == 2:
            self.poke_team_lst.insertion_sort_reverse_order()
            self.is_ascending = not self.is_ascending

    def regenerate_team(self):
        """ Regenerates the team

        :complexity: best case O(n), worst case O((n*m)+n^2)
                     where n is len(poke_team_lst) and m is len(ret_adt)

        This function resets the heal_count of the team
        generates a new PokeTeam based on the team_numbers
        """
        self.reset_heal_count()
        poke_team_lst = self._generate_poke_team()
        self.poke_team_lst = self._battle_mode_adt(poke_team_lst)

    def __str__(self):
        """ Python str magic method

        :complexity: best/worst case O(n*(K1 + K2))
                     where n is en(self.poke_team_lst) and
                     KX is the length of stringX

        This function prints out an instance of the PokeTeam class
        """
        team_member = ""
        if self.battle_mode == 0:
            temp_stack = ArrayStack(len(self.poke_team_lst))
            length = len(self.poke_team_lst)
            for idx in range(length):
                if idx < length-1:
                    pokemon = self.poke_team_lst.pop()
                    team_member += str(pokemon) + ", "
                    temp_stack.push(pokemon)
                else:
                    pokemon = self.poke_team_lst.pop()
                    team_member += str(pokemon)
                    temp_stack.push(pokemon)
            for _ in range(len(temp_stack)):
                self.poke_team_lst.push(temp_stack.pop())
        elif self.battle_mode == 1:
            for idx in range(len(self.poke_team_lst)):
                if idx < len(self.poke_team_lst)-1:
                    pokemon = self.retrieve_pokemon()
                    team_member += str(pokemon) + ", "
                    self.return_pokemon(pokemon)
                else:
                    pokemon = self.retrieve_pokemon()
                    team_member += str(pokemon)
                    self.return_pokemon(pokemon)
        elif self.battle_mode == 2:
            for idx in range(len(self.poke_team_lst)):
                if idx < len(self.poke_team_lst)-1:
                    pokemon = self.poke_team_lst[idx].value
                    team_member += str(pokemon) + ", "
                else:
                    pokemon = self.poke_team_lst[idx].value
                    team_member += str(pokemon)

        return f'{self.team_name} ({self.battle_mode}): [{team_member}]'

    def is_empty(self):
        """ Checks whether poke_team_lst is empty

        :post: poke_team_lst should not be modified
        :complexity: best case O(1)

        This function returns a boolean, false if it is not empty and true if it is
        """
        return self.poke_team_lst.is_empty()

    def choose_battle_option(self, my_pokemon: PokemonBase, their_pokemon: PokemonBase) -> Action:
        """ Allows the AI to choose the action

        :param args1: an instance of a pokemon class
        :param args2: an instance of a pokemon class

        :complexity: best/worst case O(1)

        This function allows the AI to decide an action depending on
        the pokemon currently on field and one of the 4 the logic modes chosen
        """
        if self.ai_type == PokeTeam.AI.ALWAYS_ATTACK:
            return Action.ATTACK
        elif self.ai_type == PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE:
            effective_damage = their_pokemon.calculate_damage(my_pokemon) / their_pokemon.get_attack_damage()
            if effective_damage >= 1.5:
                return Action.SWAP
            else:
                return Action.ATTACK
        elif self.ai_type == PokeTeam.AI.RANDOM:
            actions = list(Action)
            if self.heal_count >= 3:
                actions.remove(Action.HEAL)
            return actions[RandomGen.randint(0, len(actions)-1)]
        elif self.ai_type == PokeTeam.AI.USER_INPUT:
            choice = int(input("Choose an action: \n1. Attack\n2. Swap\n3. Heal\n4. Special\n"))
            return Action(choice)

    @classmethod
    def leaderboard_team(cls):
        raise NotImplementedError()
