
"""Decorator = wrapper that adds behavior (@functools.wraps is mandatory)"""

import time
import random
from functools import wraps


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper() -> callable:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func()
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power", args[0])
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> None:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"({attempt}/{max_attempts})")
                    else:
                        return (
                            f"Spell casting failed after "
                            f"{max_attempts} attempts")
            return None
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        is_valid_len = len(name) >= 3
        is_valid_chars = name.replace(" ", "").isalpha()
        return is_valid_len and is_valid_chars

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:

    # test_powers = [23, 7, 24, 14]
    spell_names = ['heal', 'meteor', 'blizzard', 'earthquake']
    # mage_names = ['River', 'Sage', 'Ash', 'Rowan', 'Alex', 'Kai']
    # invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    # Spell timer
    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"
    print("Testing spell timer...")
    print(f"Result: {fireball()}\n")

    # Power validator
    # @power_validator(10)
    # def cast_spell(power: int, spell_name: str) -> str:
    #     return f"Spell {spell_name} cast with power {power}!"
    #
    # for i in range(len(test_powers)):
    #     power = test_powers[i]
    #     name = spell_names[i]
    #     print(cast_spell(power, name))

    # Retry Spell
    @retry_spell(3)
    def loggin(name):
        if random.choice(spell_names) != name:
            raise ValueError("'{name}' not found in our database!")
        return f"Welcome back, {name}!"
    # print(loggin("blizzard"))

    # MageGuild
    guild = MageGuild()
    print("Testing MageGuild...")
    print(guild.validate_mage_name("River"))
    print(guild.validate_mage_name("Alex123"))
    print(guild.cast_spell("Lightning", power=15))
    print(guild.cast_spell("Heal", power=8))


if __name__ == "__main__":
    main()
