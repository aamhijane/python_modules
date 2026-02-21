import alchemy.transmutation.basic as basic
import alchemy.transmutation.advanced as advanced
import alchemy.transmutation

def main():
    print("=== Pathway Debate Mastery ===\n")

    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {basic.lead_to_gold()}")
    print(f"stone_to_gem(): {basic.stone_to_gem()}\n")

    print("Testing Relative Imports (from advanced.py):")
    # Note: Output matches the multiline requirement in your prompt
    print(f"philosophers_stone(): {advanced.philosophers_stone()}")
    print(f"elixir_of_life(): {advanced.elixir_of_life()}\n")

    print("Testing Package Access:")
    print(f"alchemy.transmutation.lead_to_gold(): {alchemy.transmutation.lead_to_gold()}")
    print(f"alchemy.transmutation.philosophers_stone(): {alchemy.transmutation.philosophers_stone()}\n")

    print("Both pathways work! Absolute: clear, Relative: concise")

if __name__ == "__main__":
    main()
