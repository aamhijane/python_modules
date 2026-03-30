
def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combine(target) -> tuple[str]:
        sp1 = spell1(target)
        sp2 = spell2(target)
        return (sp1, sp2)
    return combine


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def calc() -> int:
        return (base_spell() * multiplier)
    return calc


def conditional_caster(condition: callable, spell: callable) -> callable:
    def cast_spell(target: str) -> str:
        if condition(target):
            return spell(target)
        else:
            return "Spell fizzled"
    return cast_spell


def spell_sequence(spells: list[callable]) -> callable:
    spells_list = []

    def cast_all(targets: str) -> list[str]:
        if not len(spells) == len(targets):
            raise ValueError("Targets list must be equal to spells list")
        for i in range(len(spells)):
            target = f"fn {i + 1} target: {targets[i]}"
            spell = spells[i]
            spells_list.append(spell(target))
        return spells_list
    return cast_all


def main() -> None:

    try:
        def fireball(target) -> str:
            return f"Fireball hits {target}"

        def heal(target) -> str:
            return f"Heals {target}"

        combined = spell_combiner(fireball, heal)
        formated_result = str(combined('Dragon')).strip('()')
        formated_result = formated_result.replace("'", "")

        print("Testing spell combiner...")
        print(f"Combined spell result: {formated_result}\n")

        def base_spell() -> int:
            return 10

        mega_fireball = power_amplifier(base_spell, 3)

        print("Testing power amplifier...")
        print(f"Original: {base_spell()}, Amplified: {mega_fireball()}")

        # condition = lambda x: True if x == 'Fireball' else False
        # spell = lambda x: f"{x} is Ready"
        # cast_sp = conditional_caster(condition, spell)
        # print(cast_sp('Fireball'))

        # spells = [
        #     lambda x: x,
        #     lambda x: x,
        #     lambda x: x,
        #     lambda x: x,
        # ]
        # targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
        #
        # sp_seq = spell_sequence(spells)
        # cast_all = sp_seq(targets)
        # print(cast_all)
    except ValueError as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
