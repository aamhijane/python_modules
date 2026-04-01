
"""Closure = inner function remembers outer variable (nonlocal)"""


def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    total_power = initial_power

    def power_addition() -> int:
        nonlocal total_power
        total_power += initial_power
        return total_power

    return power_addition


def enchantment_factory(enchantment_type: str) -> callable:

    def enchanted_info(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchanted_info


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key):
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:

    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}\n")

    # print("Testing spell accumulator...")
    # accumulator = spell_accumulator(10)
    # print(f"Accumulation 1: {accumulator()}")
    # print(f"Accumulation 2: {accumulator()}")
    # print(f"Accumulation 3: {accumulator()}")
    print("Testing enchantment factory...")
    enchantments = {
        "Flaming": "Sword",
        "Frozen": "Shield"
    }
    for key, val in enchantments.items():
        print(enchantment_factory(key)(val))

    # vault = memory_vault()
    # vault["store"]("name", "Alice")
    #
    # print(vault["recall"]("name"))
    # print(vault["recall"]("missing"))


if __name__ == "__main__":
    main()
