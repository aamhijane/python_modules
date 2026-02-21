from .basic import lead_to_gold  # Sibling import
from ..potions import healing_potion  # Parent's sibling import

def philosophers_stone():
    return f"Philosopher's stone created using {lead_to_gold()} and {healing_potion()}"

def elixir_of_life():
    return "Elixir of life: eternal youth achieved!"
