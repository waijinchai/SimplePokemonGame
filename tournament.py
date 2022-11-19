from __future__ import annotations

"""
Implement the single elimination style tournament, team will exit the competition if any loss.
Teams will be split into even halves, and winner of each half plays against one another.
"""
__author__ = "Scaffold by Jackson Goerner, Code by Chai Wai Jin, Hang Jui Kai & Jeremy To Jun Wei"

from poke_team import PokeTeam
from battle import Battle
from linked_list import LinkedList
from stack_adt import ArrayStack
from queue_adt import CircularQueue
from random_gen import RandomGen
from bset import BSet
from pokemon_base import PokeType

class Tournament:
    """ Implements a battle tower with random PokeTeams that have a certain amount of lives for the user to face off
    against.
    """

    def __init__(self, battle: Battle|None=None) -> None:
        """ Initialisation

            :param arg1: battle logic described in the background
            :complexity: Best/Worst, O(1), since all the instructions are constant
        
            The function does initialize all the attributes.
        """
        if battle is None:
            self.battle = Battle()
        else:
            self.battle = battle
        self.battle_mode = -1
        self.tournament_queue = None
        self.tournament_str_lst = None
        self.tournament_stack = None
        self.idx = 2

    def get_battle_mode(self) -> int:
        """ To get the battle mode of PokeTeam
        
            :complexity: Best/Worst O(1), since all the instructions are constant
            
            The function returns the battle mode of PokeTeam.
        """
        return self.battle_mode

    def set_battle_mode(self, battle_mode: int) -> None:
        """ To set the battle mode of PokeTeam.

            :param arg1: battle mode of PokeTeam
            :complexity: Best/Worst O(1), since all the instructions are constant
            
            The function sets the battle mode of PokeTeam.
        """
        self.battle_mode = battle_mode

    def is_valid_tournament(self, tournament_str: str) -> bool:
        """ To verify the tournament.
        
            :pre: the string must contain at least two team name and a "+" symbol
            :post: the string should not be modified
            :param arg1: a string represent the tournaments
            :complexity: Best O(n) when tournament_str is invalid  eg. starts with a "+", Worst O(n+m) when the
                         tournament_str is valid, where n is len(tournament_str), and m is the length of the list after
                         tournament_str.split(" ").

            The function returns True if the tournament_str passed represents a valid tournament.
        """
        tournament_lst = tournament_str.split(" ")
        tournament_stack = ArrayStack(len(tournament_lst))
        for elem in tournament_lst:
            if elem != "+": 
                tournament_stack.push(elem)
            else:
                try:
                    team2 = tournament_stack.pop()
                    team1 = tournament_stack.pop()
                except Exception as e:
                    return False  # O(1)
                else:
                    battle_str = f"({team1} + {team2})"
                    tournament_stack.push(battle_str)

        return True

    def is_balanced_tournament(self, tournament_str: str) -> bool:
        # 1054 only
        raise NotImplementedError()

    def start_tournament(self, tournament_str: str) -> None:
        """ To generate the PokeTeam.
        
            :raise ValueError: if the tournament invalid
            :pre: the string must contain at least two team name and a "+" symbol
            :post: the string should not be modified
            :param arg1: a string represent the tournaments
            :complexity: Best/Worst O((n*r)+m), where n is the length of the list of tournament_str.split(" "), r is the
                         complexity of PokeTeam.random_team() method, and m is len(self.tournament_queue)
        
        """
        if not self.is_valid_tournament(tournament_str):
            raise ValueError("Tournament is not valid")

        self.tournament_str_lst = tournament_str.split(" ")
        self.tournament_queue = CircularQueue(len(self.tournament_str_lst))
        for idx in range(len(self.tournament_str_lst)):
            if self.tournament_str_lst[idx] != "+":
                self.tournament_queue.append(self.tournament_str_lst[idx])

        for _ in range(len(self.tournament_queue)):
            team = PokeTeam.random_team(self.tournament_queue.serve(), self.get_battle_mode())
            self.tournament_queue.append(team)

        self.tournament_stack = ArrayStack(len(self.tournament_queue))

    def advance_tournament(self) -> tuple[PokeTeam, PokeTeam, int] | None:
        """ To simulate the battle of tournament.

            :complexity: Best/Worst O(T+B), where T is the number of tournament battles, and B is the time complexity
                        of running a battle.
            
            The function simulates one battle of the tournament, None will be returned if no games are remaining,
            otherwise, it follows the order of the previously given tournament string.
        """
        while self.idx < len(self.tournament_str_lst) and self.tournament_str_lst[self.idx] != "+":
            self.idx += 1

        if self.idx >= len(self.tournament_str_lst):
            return None

        if self.tournament_str_lst[self.idx] == "+" and self.tournament_str_lst[self.idx-1] != "+":
            team1 = self.tournament_queue.serve()
            team2 = self.tournament_queue.serve()
        elif self.tournament_str_lst[self.idx] == "+" and self.tournament_str_lst[self.idx-1] == "+":
            team2 = self.tournament_stack.pop()
            team1 = self.tournament_stack.pop()

        battle_res = self.battle.battle(team1, team2)
        if battle_res == 1:
            team1.regenerate_team()
            self.tournament_stack.push(team1)
        else:
            team2.regenerate_team()
            self.tournament_stack.push(team2)

        res = (team1.get_team_name(), team2.get_team_name(), battle_res)
        self.idx += 1
        return res

    def linked_list_of_games(self) -> LinkedList[tuple[PokeTeam, PokeTeam]]:
        l = LinkedList()
        while True:
            res = self.advance_tournament()
            if res is None:
                break
            l.insert(0, (res[0], res[1]))
        return l
    
    def linked_list_with_metas(self) -> LinkedList[tuple[PokeTeam, PokeTeam, list[str]]]:
        """ To analyse the pokemon types.
        
            :complexity: Best/Worst O(M*(B+P)), where M is the total number of matches played, B is the time
                         complexity of running a battle, and P is the limit on the number of pokemon per team.
            
            The function returns a linked containing two PokeTeam and the types of pokemon
            which are not present in the current match's team, but are present in some of 
            the teams defeated by these players.
        """
        ret_lst = LinkedList()
        type_stack = ArrayStack(len(self.tournament_queue))
        for idx in range(len(self.tournament_str_lst)):
            if self.tournament_str_lst[idx] != "+":
                continue

            if self.tournament_str_lst[idx] == "+" and self.tournament_str_lst[idx - 1] != "+":
                team1 = self.tournament_queue.serve()
                team2 = self.tournament_queue.serve()
            elif self.tournament_str_lst[idx] == "+" and self.tournament_str_lst[idx - 1] == "+":
                team2 = self.tournament_stack.pop()
                team1 = self.tournament_stack.pop()
                previous_type = type_stack.pop()

            type_set1 = self._create_type_set(team1)
            type_set2 = self._create_type_set(team2)

            union_set = type_set1.union(type_set2)
            type_stack.push(union_set)

            battle_res = self.battle.battle(team1, team2)
            if battle_res == 1:
                team1.regenerate_team()
                self.tournament_stack.push(team1)
            else:
                team2.regenerate_team()
                self.tournament_stack.push(team2)

            ret_type_lst = []
            if self.tournament_str_lst[idx] == "+" and self.tournament_str_lst[idx - 1] == "+":
                type_res = previous_type.difference(union_set)
                for i in range(1, 6):
                    if i in type_res:
                        ret_type_lst.append(PokeType(i-1).name)

            ret_tuple = (team1, team2, ret_type_lst)
            ret_lst.insert(0, ret_tuple)

        return ret_lst

    def _create_type_set(self, team: PokeTeam) -> BSet:
        """ Creates a set that contains the Pokemon Types of a team in terms of numbers.

        :param arg: a Pokemon Team.
        :complexity: Best/Worst O(P), where P is the limit on the number of pokemon per team

        The function returns a set that contains the Pokemon Types of a team in terms of numbers.
        """
        type_set = BSet()
        for idx1 in range(len(team.get_team_numbers())):
            if team.get_team_numbers()[idx1] > 0:
                type_set.add(idx1 + 1)
        return type_set

    def flip_tournament(self, tournament_list: LinkedList[tuple[PokeTeam, PokeTeam]], team1: PokeTeam, team2: PokeTeam) -> None:
        # 1054
        raise NotImplementedError()


if __name__ == "__main__":
    RandomGen.set_seed(123456)
    t = Tournament(Battle(verbosity=0))
    t.set_battle_mode(0)
    t.start_tournament("Roark Gardenia + Maylene Crasher_Wake + Fantina Byron + + + Candice Volkner + +")
    # print(t.linked_list_of_games())
    l = t.linked_list_with_metas()
    print(l)

