"""
Contains the battle logic, allowing 2 PokeTeams to fight and returning a winner
"""
__author__ = "Scaffold by Jackson Goerner, Code by Chai Wai Jin, Hang Jui Kai & Jeremy To Jun Wei"

from random_gen import RandomGen
from poke_team import Action, PokeTeam, Criterion
from print_screen import print_game_screen
from pokemon_base import PokemonBase

class Battle:
    
    def __init__(self, verbosity=0) -> None:
        """Initialization

        :param args: an integer to indicate whether to print screen
        :complexity:
        """
        self.verbosity = verbosity

    def battle(self, team1: PokeTeam, team2: PokeTeam) -> int:
        """ Performs a battle between team1 and team2

        :pre: both teams should contain no more than 6 pokemon
        :param args1: an instance of the PokeTeam class
        :param args2: an instance of the PokeTeam class
        :complexity: Best O(T) when it is battle_mode 0 or 1 for both teams, Worst O(T(n+m)) when it is battle_mode 2
                     for both teams, where T is the total number of turns, n is len(team1.pokemon_team_lst), and m is
                     len(team2.pokemon_team_lst).
        """
        pokemon1 = team1.retrieve_pokemon()
        pokemon2 = team2.retrieve_pokemon()

        if self.verbosity != 0:
            print_game_screen(pokemon1.get_poke_name(), pokemon2.get_poke_name(), pokemon1.get_hp(), pokemon1.get_max_hp(),
                              pokemon2.get_hp(), pokemon2.get_max_hp(), pokemon1.get_level(), pokemon2.get_level(),
                              pokemon1.get_status(), pokemon2.get_status(), len(team1.poke_team_lst) + 1,
                              len(team2.poke_team_lst) + 1)

        while True:
            team1_action = team1.choose_battle_option(pokemon1, pokemon2)
            team2_action = team2.choose_battle_option(pokemon2, pokemon1)

            if team1_action == Action.SWAP:
                pokemon1 = self._perform_swap(team1, pokemon1)
            elif team1_action == Action.SPECIAL:
                pokemon1 = self._perform_special(team1, pokemon1)
            elif team1_action == Action.HEAL:
                self._perform_heal(team1, pokemon1)
                if team1.get_heal_count() > 3:
                    return 2

            if team2_action == Action.SWAP:
                pokemon2 = self._perform_swap(team2, pokemon2)
            elif team2_action == Action.SPECIAL:
                pokemon2 = self._perform_special(team2, pokemon2)
            elif team2_action == Action.HEAL:
                self._perform_heal(team2, pokemon2)
                if team2.get_heal_count() > 3:
                    return 1

            if team1_action == Action.ATTACK and team2_action == Action.ATTACK:
                pokemon1_speed = self._check_paralysis(pokemon1)
                pokemon2_speed = self._check_paralysis(pokemon2)
                if pokemon1_speed > pokemon2_speed:
                    pokemon1.attack(pokemon2)
                    if not pokemon2.is_fainted():
                        pokemon2.attack(pokemon1)
                elif pokemon1_speed < pokemon2_speed:
                    pokemon2.attack(pokemon1)
                    if not pokemon1.is_fainted():
                        pokemon1.attack(pokemon2)
                elif pokemon1_speed == pokemon2_speed:
                    pokemon1.attack(pokemon2)
                    pokemon2.attack(pokemon1)
            elif team1_action == Action.ATTACK and team2_action != Action.ATTACK:
                pokemon1.attack(pokemon2)
            elif team1_action != Action.ATTACK and team2_action == Action.ATTACK:
                pokemon2.attack(pokemon1)

            if not pokemon1.is_fainted() and not pokemon2.is_fainted():
                pokemon1.lose_hp(1)
                pokemon2.lose_hp(1)

            if pokemon1.can_evolve() and pokemon1.should_evolve() and not pokemon1.is_fainted():
                pokemon1 = self._pokemon_evolves(pokemon1)
            if pokemon2.can_evolve() and pokemon2.should_evolve() and not pokemon2.is_fainted():
                pokemon2 = self._pokemon_evolves(pokemon2)

            if not pokemon1.is_fainted() and pokemon2.is_fainted():
                if pokemon1.can_evolve() and pokemon1.should_evolve():
                    pokemon1 = self._pokemon_evolves(pokemon1)
                pokemon1.level_up()
                if pokemon1.can_evolve() and pokemon1.should_evolve():
                    pokemon1 = self._pokemon_evolves(pokemon1)
                team2.return_pokemon(pokemon2)
                try:
                    pokemon2 = team2.retrieve_pokemon()
                except Exception as e:
                    team1.return_pokemon(pokemon1)
                    return 1
                except IndexError as e:
                    team1.return_pokemon(pokemon1)
                    return 1
            elif pokemon1.is_fainted() and not pokemon2.is_fainted():
                if pokemon2.can_evolve() and pokemon2.should_evolve():
                    pokemon2 = self._pokemon_evolves(pokemon2)
                pokemon2.level_up()
                if pokemon2.can_evolve() and pokemon2.should_evolve():
                    pokemon2 = self._pokemon_evolves(pokemon2)
                team1.return_pokemon(pokemon1)
                try:
                    pokemon1 = team1.retrieve_pokemon()
                except Exception as e:
                    team2.return_pokemon(pokemon2)
                    return 2
                except IndexError as e:
                    team2.return_pokemon(pokemon2)
                    return 2
            elif pokemon1.is_fainted() and pokemon2.is_fainted():
                if team1.is_empty() and team2.is_empty():
                    return 0
                elif not team1.is_empty() and team2.is_empty():
                    return 1
                elif team1.is_empty() and not team2.is_empty():
                    return 2
                elif not team1.is_empty() and not team2.is_empty():
                    pokemon1 = team1.retrieve_pokemon()
                    pokemon2 = team2.retrieve_pokemon()

            if self.verbosity != 0:
                print_game_screen(pokemon1.get_poke_name(), pokemon2.get_poke_name(), pokemon1.get_hp(), pokemon1.get_max_hp(),
                                  pokemon2.get_hp(), pokemon2.get_max_hp(), pokemon1.get_level(), pokemon2.get_level(),
                                  pokemon1.get_status(), pokemon2.get_status(), len(team1.poke_team_lst)+1,
                                  len(team2.poke_team_lst)+1)

    def _perform_swap(self, team: PokeTeam, pokemon: PokemonBase) -> PokemonBase:
        """ Returns to current pokemon and retrieves a pokemon from the team (could be the same pokemon)

        :param args1: an instance of the PokeTeam class
        :param args2: an instance of a pokemon's class
        :complexity: Best O(1) when it is battle_mode 0 or 1, Worst O(n) when it is battle_mode 2,
                     where n is len(team.pokemon_team_lst).
        """
        team.return_pokemon(pokemon)
        return team.retrieve_pokemon()

    def _perform_special(self, team: PokeTeam, pokemon: PokemonBase) -> PokemonBase:
        """ Performs the special action depending on the battle mode chosen

        :pre PokeTeam: should be an instance of the PokeTeam class
        :post PokeTeam: order of the pokemon is the team should be shuffled depending on the battle mode chosen
        :param args1: an instance of the PokeTeam class
        :param args2: an instance of a pokemon's class
        :complexity: Best O(n) when is it battle_mode 1, Worst O(n^2) when it is battle_mode 2, where n
                     is len(team.pokemon_team_lst).
        """
        team.return_pokemon(pokemon)
        team.special()
        return team.retrieve_pokemon()

    def _perform_heal(self, team: PokeTeam, pokemon: PokemonBase) -> None:
        """ Performs the heal action, restoring a pokemon to full and clearing status effects

        :pre Pokemon: should be an instance of the pokemon's class
        :post Pokemon: the Pokemon's HP should be restored to full and status effects cleared
        :param args1: an instance of the PokeTeam class
        :param args2: an instance of a pokemon's class
        :complexity: Best/Worst O(1), everything is constant time
        """
        pokemon.heal()
        team.increment_heal_count()

    def _check_paralysis(self, pokemon: PokemonBase) -> int:
        """ Checks if the a pokemon has been inflicted with the paralysis status

        :pre: should be an instance of a pokemon's class
        :post: the speed of a pokemon should be halved if inflicted with paralysis
        :param args: an instance of a pokemon's class
        :complexity: Best/Worst O(1), everything is constant time
        """
        if pokemon.get_status() == "paralysis":
            return pokemon.get_speed() // 2
        else:
            return pokemon.get_speed()

    def _pokemon_evolves(self, pokemon: PokemonBase) -> PokemonBase:
        """ Evolves a pokemon and adjusts its stats accordingly
        
        :pre: should be an instance of the Pokemon class
        :post: should be an instance of the pokemon's evolved version's class
        :param args: an instance of a Pokemon class
        :complexity: Best/Worst O(1), every operation is constant time
        """
        status = pokemon.get_status()
        hp_diff = pokemon.get_max_hp() - pokemon.get_hp()
        pokemon = pokemon.get_evolved_version()
        pokemon.set_hp(pokemon.get_max_hp() - hp_diff)
        pokemon.set_status(status)
        if pokemon.get_status() == "paralysis":
            pokemon.set_speed(pokemon.get_speed()//2)
        return pokemon

        
if __name__ == "__main__":
    b = Battle(verbosity=3)
    RandomGen.set_seed(16)
    t1 = PokeTeam.random_team("Cynthia", 0)
    t2 = PokeTeam.random_team("Barry", 1)
    print(b.battle(t1, t2))

