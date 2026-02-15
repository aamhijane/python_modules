import sys
from typing import Dict, List


class NoArgumentError(Exception):
    """Raised when no command-line arguments are provided."""
    pass


def get_unit(qty: int) -> str:
    """Get unit(s) based on quantity."""
    if qty > 1:
        return "units"
    return "unit"


def analyze_inventory():
    try:
        """
        1. Parses a list of strings in 'name:quantity'
           format into a dictionary.
        2. Calculates the most and least abundant items in the inventory.
        3. Main execution logic to analyze and display the inventory system.
        """

        #####################################################
        # 1. Parse Arguments (input format is name:quantity)

        args: List[str] = sys.argv[1:]
        if not args:
            raise NoArgumentError("Error: No inventory items provided.")

        inventory: Dict[str, int] = {}
        total_count: int = 0

        # Populate the dictionary
        for arg in args:
            if ":" in arg:
                name, qty = arg.split(":")
                quantity = int(qty)
                inventory[name] = quantity
                total_count += quantity

        ########################################################
        # 2. Sort Inventory (by quantity, descending)

        sorted_items: List[tuple] = sorted(
                inventory.items(), key=lambda x: x[1], reverse=True)

        print("=== Inventory System Analysis ===")
        print(f"Total items in inventory: {total_count}")
        print(f"Unique item types: {len(inventory)}")

        print("\n=== Current Inventory ===")
        for name, qty in sorted_items:
            percentage: float = (qty / total_count) * 100
            print(f"{name}: {qty} {get_unit(qty)} ({percentage:.1f}%)")

        #####################################################
        # 3. Statistics: We find the min and max quantities

        max_qty: int = max(inventory.values())
        min_qty: int = min(inventory.values())

        # Find names associated with those values
        most_abundant: int = [
                k for k, v in inventory.items() if v == max_qty][0]
        least_abundant: int = [
                k for k, v in inventory.items() if v == min_qty][0]

        print("\n=== Inventory Statistics ===")
        print(f"Most abundant: {most_abundant} "
              f"({max_qty} {get_unit(max_qty)})")
        print(f"Least abundant: {least_abundant} "
              f"({min_qty} {get_unit(min_qty)})")

        # Categories
        categories: Dict[str, dict] = {"Moderate": {}, "Scarce": {}}
        for name, qty in inventory.items():
            if qty >= 5:
                categories["Moderate"].update({name: qty})
            else:
                categories["Scarce"].update({name: qty})

        print("\n=== Item Categories ===")
        print(f"Moderate: {categories.get('Moderate')}")
        print(f"Scarce: {categories.get('Scarce')}")

        # Management Suggestions
        restock: List[str] = [
                name for name, qty in inventory.items() if qty <= 1]
        print("\n=== Management Suggestions ===")
        print(f"Restock needed: {restock}")

        # Dictionary Properties Demo
        print("\n=== Dictionary Properties Demo ===")
        print(f"Dictionary keys: {', '.join(inventory.keys())}")
        # Convert map object to list of strings for printing
        print(f"Dictionary values: {', '.join(map(str, inventory.values()))}")
        print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")
    except NoArgumentError as e:
        print(e)
    except ValueError:
        print("Error: Invalid quantity format. Use 'name:number'.")


if __name__ == "__main__":
    analyze_inventory()
