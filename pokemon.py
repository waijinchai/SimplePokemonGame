from pokemon_base import PokemonBase, PokeType

"""
Implement the attributes of each Pokemon.
"""
__author__ = "Scaffold by Jackson Goerner, Code by Chai Wai Jin, Hang Jui Kai & Jeremy To Jun Wei"

class Charizard(PokemonBase):
    """Implement the attributes of Charizard and methods to calculate its defense, level up and evolving"""

    BASE_HP = 12
    BASE_ATTACK = 10
    BASE_SPD = 9
    BASE_DEF = 4
    
    def __init__(self) -> None:
        """ Initialisation
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations for the attributes of Charizard.
        """
        PokemonBase.__init__(self, PokeType.FIRE, "Charizard", 3)
        self.hp = Charizard.BASE_HP + (1 * self.get_level())
        self.attack_damage = self.BASE_ATTACK + (2 * self.get_level())
        self.speed = self.BASE_SPD + (1 * self.get_level())
        self.defence = self.BASE_DEF
        self.max_hp = self.get_hp()

    def level_up(self) -> None:
        """ Increases the level of the pokemon
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations again to calculate the new attributes for the leveled up Charizard.

        """
        PokemonBase.level_up(self)
        self.hp = self.BASE_HP + (1 * self.get_level()) - (self.max_hp - self.get_hp())
        self.attack_damage = self.BASE_ATTACK + (2 * self.get_level())
        self.speed = self.BASE_SPD + (1 * self.get_level())
        self.max_hp = self.BASE_HP + (1 * self.get_level())

    def defend(self, damage: int) -> None:
        """ To calculate how the Pokemon reacts when being attacked with effective attack points.

            :param arg1: effective attack points
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The functino does the calculations to find the amount of damage the Charizard takes.Charizard 
            takes double the damage if the effective damage is more than the defence, otherwise it loses 
            HP equal to the attack.
        """
        if damage > self.get_defence():
            self.lose_hp((damage * 2))
        else:
            self.lose_hp(damage)

    def should_evolve(self) -> bool:
        """ To indicate that the Pokemon should evolve.

            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns false as Charizard cannot evolve any further.
        """
        return False

    def can_evolve(self) -> bool:
        """ To indicate that the Pokemon can evolve.

            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns false as Charizard cannot evolve any further.
        """
        return False

    def get_evolved_version(self) -> PokemonBase:
        """ Get the evolved version of the pokemon.

            :raise ValueError: Charizard cannot further evolve
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function raises a ValueError as this pokemon cannot evolve.
        """
        raise ValueError("This Pokemon cannot evolve")

class Charmander(PokemonBase):
    """Implement the attributes of Charmander and methods to calculate its defense, level up and evolving"""

    BASE_HP = 8
    BASE_ATTACK = 6
    BASE_SPD = 7
    BASE_DEF = 4
    
    def __init__(self) -> None:
        """ Initialisation
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations for the attributes of Charmander.
        """
        PokemonBase.__init__(self, PokeType.FIRE, "Charmander", 1)
        self.hp = self.BASE_HP + (1 * self.get_level())
        self.attack_damage = self.BASE_ATTACK + (1 * self.get_level())
        self.speed = self.BASE_SPD + (1 * self.get_level())
        self.defence = self.BASE_DEF
        self.max_hp = self.get_hp()

    def level_up(self) -> None:
        """ Increases the level of the pokemon
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations again to calculate the new attributes for the leveled up Charmander.
        """
        PokemonBase.level_up(self)
        self.hp = self.BASE_HP + (1 * self.get_level()) - (self.max_hp - self.get_hp())
        self.attack_damage = self.BASE_ATTACK + (1 * self.get_level())
        self.speed = self.BASE_SPD + (1 * self.get_level())
        self.max_hp = self.BASE_HP + (1 * self.get_level())

    def defend(self, damage: int) -> None:
        """ To calculate how the Pokemon reacts when being attacked with effective attack points.
        
            :param arg1: effective attack points
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations to find the amount of damage the Charmander takes. Charmander 
            loses HP equal to the attack if the effective damage is more than the defence, otherwise it 
            loses HP equal to half the attack
        """
        if damage > self.get_defence():
            self.lose_hp(damage)
        else:
            self.lose_hp((damage // 2))

    def should_evolve(self) -> bool:
        """ To indicate that the Pokemon should evolve.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns True if the level of Pokemon is greater or equal to 3, else returns False.
        """
        return self.get_level() >= 3

    def can_evolve(self) -> bool:
        """ To indicate that the Pokemon can evolve.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns True as Charmander can evolve.
        """
        return True

    def get_evolved_version(self) -> PokemonBase:
        """ Get the evolved version of the pokemon.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns the Charizard class as Charmander can evolve into Charizard
        """
        return Charizard()

class Venusaur(PokemonBase):
    """Implement the attributes of Venusaur and methods to calculate its defense, level up and evolving"""

    BASE_HP = 20
    BASE_ATTACK = 5
    BASE_SPD = 3
    BASE_DEF = 10
    
    def __init__(self) -> None:
        """ Initialisation
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations for the attributes of Venusaur.
        """
        PokemonBase.__init__(self, PokeType.GRASS, "Venusaur", 2)
        self.hp = self.BASE_HP + (self.get_level() // 2)
        self.attack_damage = self.BASE_ATTACK
        self.speed = self.BASE_SPD + (self.get_level() // 2)
        self.defence = self.BASE_DEF
        self.max_hp = self.get_hp()
        
    def level_up(self) -> None:
        """ Increases the level of the pokemon
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations again to calculate the new attributes for the leveled up Venusaur.
        """
        PokemonBase.level_up(self)
        self.hp = self.BASE_HP + (self.get_level() // 2) - (self.max_hp - self.get_hp())
        self.speed = self.BASE_SPD + (self.get_level() // 2)
        self.max_hp = self.BASE_HP + (self.get_level() // 2)

    def defend(self, damage: int) -> None:
        """ To calculate how the Pokemon reacts when being attacked with effective attack points.

            :param arg1: effective attack points
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations to find the amount of damage the Venusaur takes. Venusaur loses 
            HP equal to the attack if the effective damage is more than the (defence + 5), otherwise it loses 
            HP equal to half the attack
        """
        if damage > (self.get_defence() + 5):
            self.lose_hp(damage)
        else:
            self.lose_hp((damage // 2))

    def should_evolve(self) -> bool:
        """ To indicate that the Pokemon should evolve.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns False as Venusaur cannot evolve any further.
        """
        return False

    def can_evolve(self) -> bool:
        """ To indicate that the Pokemon can evolve.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns False as Venusaur cannot evolve.
        """
        return False

    def get_evolved_version(self) -> PokemonBase:
        """ Get the evolved version of the pokemon.
        
            :raise ValueError: Venusaur cannot further evolve
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function raises an error as Venusaur cannot evolve.
         """
        raise ValueError("This Pokemon cannot evolve")

class Bulbasaur(PokemonBase):
    """Implement the attributes of Bulbasaur and methods to calculate its defense, level up and evolving"""
    BASE_HP = 12
    BASE_ATTACK = 5
    BASE_SPD = 7
    BASE_DEF = 5
    
    def __init__(self) -> None:
        """ Initialisation
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations for the attributes of Bulbasaur.
        """
        PokemonBase.__init__(self, PokeType.GRASS, 'Bulbasaur', 1)
        self.hp = self.BASE_HP + (1 * self.get_level())
        self.attack_damage = self.BASE_ATTACK
        self.speed = self.BASE_SPD + (self.get_level() // 2)
        self.defence = self.BASE_DEF
        self.max_hp = self.get_hp()
        
    def level_up(self) -> None:
        """ Increases the level of the pokemon
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations again to calculate the new attributes for the leveled up Bulbasaur.
        """
        PokemonBase.level_up(self)
        self.hp = self.BASE_HP + (1 * self.get_level()) - (self.max_hp - self.get_hp())
        self.speed = self.BASE_SPD + (self.get_level() // 2)
        self.max_hp = self.BASE_HP + (1 * self.get_level())

    def defend(self, damage: int) -> None:
        """ To calculate how the Pokemon reacts when being attacked with effective attack points.

            :param arg1: effective attack points
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function roes the calculations to find the amount of damage the Bulbasaur takes. Bulbasaur loses HP 
            equal to the attack if the effective damage is more than the defence, otherwise it loses HP equal to 
            half the attack.
        """
        if damage > (self.get_defence() + 5):
            self.lose_hp(damage)
        else:
            self.lose_hp((damage // 2))

    def should_evolve(self) -> bool:
        """ To indicate that the Pokemon should evolve.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns True if the level of Pokemon is greater or equal to 2, else returns False.
        """
        return self.get_level() >= 2

    def can_evolve(self) -> bool:
        """ To indicate that the Pokemon can evolve.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns True as Bulbasaur can evolve.
        """
        return True

    def get_evolved_version(self) -> PokemonBase:
        """ Get the evolved version of the pokemon.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

           The function returns the Venusaur class as Bulbasaur can evolve into Venusaur.
       """
        return Venusaur()

class Blastoise(PokemonBase):
    """Implement the attributes of Blastoise and methods to calculate its defense, level up and evolving"""

    BASE_HP = 15
    BASE_ATTACK = 8
    BASE_SPD = 10
    BASE_DEF = 8
    
    def __init__(self) -> None:
        """ Initialisation
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations for the attributes of Blastoise.
        """
        PokemonBase.__init__(self, PokeType.WATER, 'Blastoise', 3)
        self.hp = self.BASE_HP + (2 * self.get_level())
        self.attack_damage = self.BASE_ATTACK + (self.get_level() // 2)
        self.speed = self.BASE_SPD
        self.defence = self.BASE_DEF + (1 * self.get_level())
        self.max_hp = self.get_hp()
    
    def level_up(self) -> None:
        """ Increases the level of the pokemon
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations again to calculate the new attributes for the leveled up Blastoise.
       """
        PokemonBase.level_up(self)
        self.hp = self.BASE_HP + (2 * self.get_level()) - (self.max_hp - self.get_hp())
        self.attack_damage = self.BASE_ATTACK + (self.get_level() // 2)
        self.defence = self.BASE_DEF + (1 * self.get_level())
        self.max_hp = self.BASE_HP + (2 * self.get_level())
        
    def defend(self, damage: int) -> None:
        """ To calculate how the Pokemon reacts when being attacked with effective attack points.

            :param arg1: effective attack points
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations to find the amount of damage the Blastoise takes. Blastoise loses HP 
            equal to twice the attack if the effective damage is more than the defence, otherwise it loses HP equal 
            to the attack.
        """
        if damage > (self.get_defence() * 2):
            self.lose_hp(damage)
        else:
            self.lose_hp((damage // 2))

    def should_evolve(self) -> bool:
        """ To indicate that the Pokemon should evolve.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns False as Blastoise cannot evolve any further.
        """
        return False

    def can_evolve(self) -> bool:
        """ To indicate that the Pokemon can evolve.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns False as Blastoise cannot evolve.
        """
        return False

    def get_evolved_version(self) -> PokemonBase:
        """ Get the evolved version of the pokemon.

            :raise ValueError: Blastoise cannot further evolve
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function raises an error as Blastoise cannot evolve.
         """
        raise ValueError("This Pokemon cannot evolve")

class Squirtle(PokemonBase):
    """Implement the attributes of Squirtle and methods to calculate its defense, level up and evolving"""

    BASE_HP = 9
    BASE_ATTACK = 4
    BASE_SPD = 7
    BASE_DEF = 6
    
    def __init__(self) -> None:
        """ Initialisation
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations for the attributes of Squirtle.
        """
        PokemonBase.__init__(self, PokeType.WATER, 'Squirtle', 1)
        self.hp = self.BASE_HP + (2 * self.get_level())
        self.attack_damage = self.BASE_ATTACK + (self.get_level() // 2)
        self.speed = self.BASE_SPD
        self.defence = self.BASE_DEF + (self.get_level())
        self.max_hp = self.get_hp()
        
    def level_up(self) -> None:
        """ Increases the level of the pokemon
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations again to calculate the new attributes for the leveled up Squirtle.
        """
        PokemonBase.level_up(self)
        self.hp = self.BASE_HP + (2 * self.get_level()) - (self.max_hp - self.get_hp())
        self.attack_damage = self.BASE_ATTACK + (self.get_level() // 2)
        self.defence = self.BASE_DEF + self.get_level()
        self.max_hp = self.BASE_HP + (2 * self.get_level())
    
    def defend(self, damage: int) -> None:
        """ To calculate how the Pokemon reacts when being attacked with effective attack points.
        
            :param arg1: effective attack points
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations to find the amount of damage the Squirtle takes. Squirtle loses HP 
            equal to the attack if the effective damage is more than twice the defence, otherwise it loses HP 
            equal to half the attack.
        """
        if damage > (self.get_defence() * 2):
            self.lose_hp(damage)
        else:
            self.lose_hp((damage // 2))

    def should_evolve(self) -> bool:
        """ To indicate that the Pokemon should evolve.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns True if the level of Pokemon is greater or equal to 3, else returns False.
        """
        return self.get_level() >= 3

    def can_evolve(self) -> bool:
        """ To indicate that the Pokemon can evolve.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns True as Squirtle can evolve
        """
        return True

    def get_evolved_version(self) -> PokemonBase:
        """ Get the evolved version of the pokemon.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns the Blastoise class as Squirtle can evolve into Blastoise
        """
        return Blastoise()

class Gengar(PokemonBase):
    """Implement the attributes of Gengar and methods to calculate its defense, level up and evolving"""

    BASE_HP = 12
    BASE_ATTACK = 18
    BASE_SPD = 12
    BASE_DEF = 3

    def __init__(self) -> None:
        """ Initialisation
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations for the attributes of Gengar.
        """
        PokemonBase.__init__(self, PokeType.GHOST, "Gengar", 3)
        self.hp = self.BASE_HP + (self.get_level() // 2)
        self.attack_damage = self.BASE_ATTACK
        self.speed = self.BASE_SPD
        self.defence = self.BASE_DEF
        self.max_hp = self.get_hp()
        
    def level_up(self) -> None:
        """ Increases the level of the pokemon

            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations again to calculate the new attributes for the leveled up Gengar.
        """
        PokemonBase.level_up(self)
        self.hp = self.BASE_HP + (self.get_level() // 2) - (self.max_hp - self.get_hp())
        self.max_hp = self.BASE_HP + (self.get_level() // 2)

    def defend(self, damage: int) -> None:
        """ To calculate how the Pokemon reacts when being attacked with effective attack points.

            :param arg1: effective attack points
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations to find the amount of damage the Gengar takes. Gengar loses HP equal 
            to the attack.
        """
        self.lose_hp(damage)

    def should_evolve(self) -> bool:
        """ To indicate that the Pokemon should evolve.

            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns False as Gengar cannot evolve any further.
        """
        return False

    def can_evolve(self) -> bool:
        """ To indicate that the Pokemon can evolve.

            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns False as Gengar cannot evolve.
        """
        return False

    def get_evolved_version(self) -> PokemonBase:
        """ Get the evolved version of the pokemon.

            :raise ValueError: Gengar cannot further evolve
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function raises an error as Gengar cannot evolve.
        """
        raise ValueError("This Pokemon cannot evolve")

class Haunter(PokemonBase):
    """Implement the attributes of Haunter and methods to calculate its defense, level up and evolving"""

    BASE_HP = 9
    BASE_ATTACK = 8
    BASE_SPD = 6
    BASE_DEF = 6

    def __init__(self) -> None:
        """ Initialisation
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations for the attributes of Haunter.
        """
        PokemonBase.__init__(self, PokeType.GHOST, "Haunter", 1)
        self.hp = self.BASE_HP + (self.get_level() // 2)
        self.attack_damage = self.BASE_ATTACK
        self.speed = self.BASE_SPD
        self.defence = self.BASE_DEF
        self.max_hp = self.get_hp()
        
    def level_up(self) -> None:
        """ Increases the level of the pokemon
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations again to calculate the new attributes for the leveled up Haunter.

        """
        PokemonBase.level_up(self)
        self.hp = self.BASE_HP + (self.get_level() // 2) - (self.max_hp - self.get_hp())
        self.max_hp = self.BASE_HP + (self.get_level() // 2)

    def defend(self, damage: int) -> None:
        """ To calculate how the Pokemon reacts when being attacked with effective attack points.

            :param arg1: effective attack points
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations to find the amount of damage the Haunter takes. Haunter loses HP 
            equal to the attack.
        """
        self.lose_hp(damage)

    def should_evolve(self) -> bool:
        """ To indicate that the Pokemon should evolve.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns True if the level of Pokemon is greater or equal to 3, else returns False.
        """
        return self.get_level() >= 3

    def can_evolve(self) -> bool:
        """ To indicate that the Pokemon can evolve.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns True as Haunter can evolve.
        """
        return True

    def get_evolved_version(self) -> PokemonBase:
        """ Get the evolved version of the pokemon.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.
            
            The function returns the Gengar class as Haunter can evolve into Gengar.
        """
        return Gengar()

class Gastly(PokemonBase):
    """Implement the attributes of Gastly and methods to calculate its defense, level up and evolving"""

    BASE_HP = 6
    BASE_ATTACK = 4
    BASE_SPD = 2
    BASE_DEF = 8    

    def __init__(self) -> None:
        """ Initialisation
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations for the attributes of Gastly.
        """
        PokemonBase.__init__(self, PokeType.GHOST, "Gastly", 1)
        self.hp = self.BASE_HP + (self.get_level() // 2)
        self.attack_damage = self.BASE_ATTACK
        self.speed = self.BASE_SPD
        self.defence = self.BASE_DEF
        self.max_hp = self.get_hp()
        
    def level_up(self) -> None:
        """ Increases the level of the pokemon
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations again to calculate the new attributes for the leveled up Gastly.

        """
        PokemonBase.level_up(self)
        self.hp = self.BASE_HP + (self.get_level() // 2) - (self.max_hp - self.get_hp())
        self.max_hp = self.BASE_HP + (self.get_level() // 2)

    def defend(self, damage: int) -> None:
        """ To calculate how the Pokemon reacts when being attacked with effective attack points.

            :param arg1: effective attack points
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations to find the amount of damage the Gastly takes. Gastly loses HP 
            equal to the attack.
        """
        self.lose_hp(damage)

    def should_evolve(self) -> bool:
        """ To indicate that the Pokemon should evolve.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns True if the level of Pokemon is greater or equal to 1, else returns False.
        """
        return self.get_level() >= 1

    def can_evolve(self) -> bool:
        """ To indicate that the Pokemon can evolve.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns True as Gastly can evolve.
        """
        return True

    def get_evolved_version(self) -> PokemonBase:
        """ Get the evolved version of the pokemon.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns the Haunter class as Gastly can evolve into Haunter.
        """
        return Haunter()


class Eevee(PokemonBase):
    """Implement the attributes of Eevee and methods to calculate its defense, level up and evolving"""
    
    BASE_HP = 10
    BASE_ATTACK = 6
    BASE_SPD = 7
    BASE_DEF = 4

    def __init__(self) -> None:
        """ Initialisation
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations for the attributes of Eevee.
        """
        PokemonBase.__init__(self, PokeType.NORMAL, "Eevee", 1)
        self.hp = self.BASE_HP
        self.attack_damage = self.BASE_ATTACK + self.get_level()
        self.speed = self.BASE_SPD + self.get_level()
        self.defence = self.BASE_DEF + self.get_level()
        self.max_hp = self.get_hp()
        
    def level_up(self) -> None:
        """ Increases the level of the pokemon
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations again to calculate the new attributes for the leveled up Eevee.
        """
        PokemonBase.level_up(self)
        self.attack_damage = self.BASE_ATTACK + self.get_level()
        self.speed = self.BASE_SPD + self.get_level()
        self.defence = self.BASE_DEF + self.get_level()

    def defend(self, damage: int) -> None:
        """ To calculate how the Pokemon reacts when being attacked with effective attack points.
        
            :param arg1: effective attack points
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function does the calculations to find the amount of damage the Eevee takes. Eevee loses HP 
            equal to the attack if the effective damage is more than the defence, otherwise it does not lose 
            any HP.
        """
        if damage >= self.get_defence():
            self.lose_hp(damage)

    def should_evolve(self) -> bool:
        """ To indicate that the Pokemon should evolve.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns False as Eevee cannot evolve.
        """
        return False

    def can_evolve(self) -> bool:
        """ To indicate that the Pokemon can evolve.
        
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function returns False as Eevee cannot any further.
        """
        return False

    def get_evolved_version(self) -> PokemonBase:
        """ Get the evolved version of the pokemon.
        
            :raise ValueError: Eevee cannot further evolve
            :complexity: Best/Worst O(1), since all intrusctions are constant.

            The function raises ValueError as Eevee does not evolve into any pokemon.
        """
        raise ValueError("This Pokemon cannot evolve")
