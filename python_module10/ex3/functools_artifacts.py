from functools import partial, reduce, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    result = 0

    if operation == "add":
        result = reduce(add, spells)
        print(f"Sum: {result}")
    elif operation == "multiply":
        result = reduce(mul, spells)
        print(f"Product: {result}")
    elif operation == "max":
        result = max(spells)
        print(f"Max: {result}")
    elif operation == "min":
        result = min(spells)
        print(f"Min: {result}")
    else:
        raise ValueError("Invalid operation!")

    return result


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, power=50, element="fire"),
        "ice_enchant": partial(base_enchantment, power=50, element="ice"),
        "lightning_enchant": partial(base_enchantment, power=50, element="lightning")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:

    @singledispatch(int)
    def _(spell: int):
        return f"The damage spell: {spell}"



def main() -> None:
    spell_powers = [15, 16, 32, 40]
    operations = ['add', 'multiply', 'max']
    fibonacci_tests = [14, 8, 20, 10]

    print("Testing spell reducer...")
    try:
        for op in operations:
            spell_reducer(spell_powers, op)
        
        print("\nTesting memoized fibonacci...")
        for fib in fibonacci_tests:
            print(f"Fib({fib}): {memoized_fibonacci(fib)}")
    except ValueError as e:
        print(f"ERROR: {e}")

    # def enchant(power, element, target):
    #     return f"{target} is enchanted with {element} power {power}!"
    #
    # enchants = partial_enchanter(enchant)
    # print(enchants['fire_enchant'](target="Goblin"))
    # print(enchants['ice_enchant'](target="Dragon"))
    # print(enchants['lightning_enchant'](target="Troll"))




if __name__ == "__main__":
    main()
