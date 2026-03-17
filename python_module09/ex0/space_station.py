from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(None, max_length=200)


def main() -> None:
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2024-05-01T12:00:00",
    )

    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: "
          f"{'Operational' if station.is_operational else 'Maintenance'}")

    print("\n========================================")
    print("Expected validation error:")
    try:
        invalid_station = SpaceStation(
            station_id="BAD001",
            name="Overloaded Station",
            crew_size=30,
            power_level=50.0,
            oxygen_level=80.0,
            last_maintenance="2024-05-01T12:00:00"
        )
        print(f"New Crew: {invalid_station.crew_size} people")
    except ValidationError as e:
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
