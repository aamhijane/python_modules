"""Module for recording spells in the master grimoire."""

def get_recording_status():
    return "Ready"

def record_spell(spell_name: str, ingredients: str) -> str:
    # Late import: The 'curse' is broken because validator isn't 
    # loaded until record_spell is actually called.
    from .validator import validate_ingredients
    
    validation_result = validate_ingredients(ingredients)
    
    # Check if validation passed to determine the correct prefix
    if "INVALID" in validation_result:
        return f"Spell rejected: {spell_name} ({validation_result})"
    
    return f"Spell recorded: {spell_name} ({validation_result})"
