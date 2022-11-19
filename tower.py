from __future__ import annotations

""" 
Generates random pokemon teams and gives them a certain number of lives
Your own teams faces then generated teams off
If you win/draw, the opposing team loses a life, if you lose, the tower finishes 
Once all opposing teams have 0 lives, the tower is complete and you are victorious
"""
__author__ = "Scaffold by Jackson Goerner, Code by Chai Wai Jin, Hang Jui Kai & Jeremy To Jun Wei"

from poke_team import PokeTeam, Criterion
from battle import Battle
from random_gen import RandomGen
from linked_list import *
from sorted_list import ListItem
from queue_adt import CircularQueue

class BattleTower:

    def __init__(self, battle: Battle|None=None) -> None:
        """Initialization
        
            :pre: battle should be an instance of the Battle class
            :post: it should not be modified
            :param args: battle logic described in the background
            :complexity: Best/Worst O(1), since every operation is constant time
        """
        self.battle = battle
        self.my_team = None
        self.tower_team_lst = None

    def get_my_team(self) -> PokeTeam:
        """ Returns the team
            
            :complexity: Best/Worst O(1), since every operation is constant time
        """
        return self.my_team

    def get_tower_team_lst(self) -> LinkedList:
        """ Returns the tower team list
            
            :complexity: Best/Worst O(1), since every operation is constant time
        """
        return self.tower_team_lst
    
    def set_my_team(self, team: PokeTeam) -> None:
        """ Sets the PokeTeam
        
            :pre: team must be an instance of the PokeTeam class
            :post: it should not be modified
            :param args: a team of pokemons
            :complexity: Best/Worst O(1), since every operation is constant time
        """
        self.my_team = team

    def set_tower_team(self, lst: LinkedList) -> None:
        """ Sets the PokeTeam
        
            :pre: linked list should contain only PokeTeams and integers representing number of lives
            :post: linked list should not be modified
            :param args: a linked list of PokeTeams and number of lives
            :complexity: Best/Worst O(1), since every operation is constant time
        """
        self.tower_team_lst = lst
    
    def generate_teams(self, n: int) -> None:
        """ Generates a random PokeTeam
        
            :pre: n should be an integer more than 0
            :post: n should not be modified
            :param args: an integer indicating the number of teams to generate
            :raises ValueError: if the argument is not integer or more than 0
            :complexity: Best/Worst O(n), where n is the number of teams to be generated
        """
        if not type(n) == int or n < 0:
            raise ValueError("number must be a positive integer")

        self.tower_team_lst = CircularQueue(n)
        for i in range(n):  # O(n), n is the number of teams to generate
            battle_mode = RandomGen.randint(0, 1)
            team = PokeTeam.random_team(f"Team {i}", battle_mode)
            no_of_lives = RandomGen.randint(2, 10)
            self.tower_team_lst.append(ListItem(team, no_of_lives))

    def __iter__(self):
        """ Magic method returns an iterator object that goes through each element of the given object. """
        return BattleTowerIterator(self)

class BattleTowerIterator:

    def __init__(self, battle_tower) -> None:
        """ Initialization
        
            :param args: an instance of the BattleTower class
            :complexity: Best/Worst O(1), since all operations are constant
        """
        self.battle_tower = battle_tower
        self.current = 0
        self.defeat = False

    def __iter__(self):
        """ Magic method returns an iterator object that goes through each element of the given object. """
        return self

    def __next__(self):
        """ Performs one battle in the tower and returns a tuple containing the results
        
            :raises StopIteration: stops the method if the user has been defeated or no more opponents remain
            :complexity: Best/Worst O(B), where B is the complexity of battle.
        """
        player_team = self.battle_tower.get_my_team()
        tower_team_lst = self.battle_tower.get_tower_team_lst()

        if not tower_team_lst.is_empty() and not self.defeat:
            tower_team = tower_team_lst.serve()

            player_team.regenerate_team()
            tower_team.value.regenerate_team()
            battle_res = self.battle_tower.battle.battle(player_team, tower_team.value)

            if battle_res == 1:
                tower_team.key -= 1
            else:
                self.defeat = True

            remaining_lives = tower_team.key
            if tower_team.key != 0:
                tower_team_lst.append(tower_team)

            res = (battle_res, player_team, tower_team.value, remaining_lives)
            return res
        else:
            raise StopIteration

    def avoid_duplicates(self):
        """ Removes all currently alive trainers who have multiple pokemon of the same type
            
            :complexity: Best/Worst O(N*P), where N is the number of trainers remaining in the battle tower and
                         P is the limit on the number of pokemon per team.
        """
        tower_lst = self.battle_tower.get_tower_team_lst()
        for _ in range(len(tower_lst)):
            count = 0
            team = tower_lst.serve()
            for num in team.value.get_team_numbers():
                if num > 1:
                    count += 1
            if count == 0:
                tower_lst.append(team)

    def sort_by_lives(self):
        # 1054
        raise NotImplementedError()


if __name__ == "__main__":
    RandomGen.set_seed(29183712400123)

    bt = BattleTower(Battle(verbosity=0))
    bt.set_my_team(PokeTeam.random_team("Jackson", 0, team_size=6))
    bt.generate_teams(10)

    it = iter(bt)
    it.avoid_duplicates()


