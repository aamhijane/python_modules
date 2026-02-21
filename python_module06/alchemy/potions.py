from .elements import create_fire, create_water, create_earth

def healing_potion():
    return f"Healing potion brewed with {create_fire()} and {create_water()}"

def strength_potion():
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"
