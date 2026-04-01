
"""Lambda = short anonymous function (map, filter, sorted)"""

from typing import List, Dict, Union


def artifact_sorter(
    artifacts: List[Dict[str, Union[str, int]]]
) -> List[Dict[str, Union[str, int]]]:

    if not artifacts:
        raise ValueError("Artifatcs list must not be empty!")

    sorted_by_power = sorted(
        artifacts,
        key=lambda artifact: artifact['power'],
        reverse=True
    )
    return sorted_by_power


def power_filter(
    mages: List[Dict[str, Union[str, int]]],
    min_power: int
) -> List[Dict[str, Union[str, int]]]:

    if not mages:
        raise ValueError("Mages list must not be empty!")

    filtered_by_power = list(filter(
        lambda mage: mage['power'] >= min_power,
        mages
    ))
    return filtered_by_power


def spell_transformer(
    spells: List[str]
) -> List[str]:

    if not spells:
        raise ValueError("Spells list must not be empty!")

    transformed_spells = list(map(
        lambda spell: "* " + spell + " *",
        spells
    ))
    return transformed_spells


def mage_stats(
    mages: List[Dict[str, Union[str, int]]]
) -> Dict[str, Union[int, float]]:

    if not mages:
        raise ValueError("Mages list must not be empty!")

    max_power = max(mages, key=lambda m: m['power'])['power']
    min_power = min(mages, key=lambda m: m['power'])['power']
    avg_power = round(
        sum(map(lambda m: m['power'], mages)) / len(mages), 2
    )

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


def main() -> None:

    artifacts = [
        {"name": "Light Prism", "power": 97, "type": "focus"},
        {"name": "Ice Wand", "power": 71, "type": "accessory"},
        {"name": "Shadow Blade", "power": 112, "type": "accessory"},
        {"name": "Storm Crown", "power": 80, "type": "weapon"},
    ]
    spells = ["meteor", "blizzard", "earthquake", "flash"]
    # mages = [
    #     {"name": "Jordan", "power": 53, "element": "light"},
    #     {"name": "Jordan", "power": 87, "element": "water"},
    #     {"name": "Kai", "power": 62, "element": "earth"},
    #     {"name": "Alex", "power": 78, "element": "light"},
    #     {"name": "Ash", "power": 98, "element": "shadow"},
    # ]

    try:
        # Testing artifact sorted data
        print("Testing artifact sorter...")
        st_artifacts = artifact_sorter(artifacts)
        name = st_artifacts[0]['name']
        power = st_artifacts[0]['power']
        artifact_result = f"{name} ({power} power)"
        if len(st_artifacts) > 1:
            name = st_artifacts[1]['name']
            power = st_artifacts[1]['power']
            artifact_result += f" comes before {name} ({power} power)"
        print(artifact_result)

        # Testing spell transformer data ...
        print("\nTesting spell transformer...")
        tr_spells = spell_transformer(spells)
        print(' '.join(sp for sp in tr_spells))
    except ValueError as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
