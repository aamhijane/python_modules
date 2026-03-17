import json
import random
import os
import sys
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def check_business_rules(self) -> "AlienContact":
        # contact_id must start with "AC".
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                    "Contact ID must be starts with 'AC'")
        # If contact_type is PHYSICAL, then is_verified must be True.
        if (
            self.contact_type == ContactType.PHYSICAL
            and not self.is_verified
        ):
            raise ValueError(
                    "Physical contact must be verified")
        # If contact_type is TELEPATHIC, then
        # witness_count must be at least 3.
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                    "Telepathic contact requires at least 3 witnesses")
        # If signal_strength > 7.0, then
        # message_received must not be empty/None.
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                    "Message field must not be empty/None")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    # data path
    data_path: str = "../generated_data/alien_contacts.json"

    try:
        # check if data file exist
        if not os.path.exists(data_path):
            raise FileNotFoundError("Data file not found in root directory")

        # Open and load the JSON (expecting a list of dicts)
        with open(data_path, "r", encoding="utf-8") as f:
            raw_contacts = json.load(f)

        # Pick random valid contact
        raw: dict = random.choice(raw_contacts)

        # Create Alien contact
        contact = AlienContact(**raw)

        # If valid, print a short summary
        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: {contact.message_received!r}")

        # If invalid, show validation errors
        print("\n======================================")
        print("Expected validation error:")
        AlienContact(
            contact_id="AC_BAD_01",
            timestamp="2024-01-01T13:00:00",
            location="Unknown sector",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=5.0,
            duration_minutes=30,
            witness_count=1,
            message_received=None,
            is_verified=False,
        )
    except ValidationError as e:
        err_msg: str = e.errors()[0]['msg']
        # Remove 'Value error' from error message
        if "Value error" in err_msg:
            err_msg = err_msg.replace("Value error, ", "")
        print(err_msg)
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
