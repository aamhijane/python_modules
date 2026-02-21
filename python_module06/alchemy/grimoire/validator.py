"""Module for validating alchemical ingredients."""

def validate_ingredients(ingredients: str) -> str:
    # Late import to break circular dependency
    from .spellbook import get_recording_status
    
    status = get_recording_status()
    valid_ingredients = ["fire air", "air"]
    
    if status == "Ready" and ingredients in valid_ingredients:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
