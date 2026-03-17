import random
from enum import Enum
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validation_rules(self) -> "SpaceMission":

        # Mission ID must starts with 'M'
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must be starts with 'M' character")

        # Mission must have at least one commander or captin
        any_rank: bool = False
        for member in self.crew:
            if member.rank.value in ["commander", "captain"]:
                any_rank = True
                break
        if not any_rank:
            raise ValueError(
                "Mission must have at least one Commander or Captain")

        # Check if 50% of crew members have 5+ years of exp
        if self.duration_days > 365:
            # Formula: number of 5+ years exp members / total crew members
            five_exp_members: int = sum(
                    1 for m in self.crew if m.years_experience >= 5)
            percentage_of_exp = (five_exp_members / len(self.crew)) * 100

            if percentage_of_exp < 50:
                raise ValueError(
                    "Long missions (> 365 days) "
                    "need 50% experienced crew (5+ years)"
                )

        # Check if all crew members active
        for memb in self.crew:
            if not memb.is_active:
                raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    SPACE_MISSIONS: list = [
        {
            'mission_id': 'M2024_TITAN',
            'mission_name': 'Solar Observatory Research Mission',
            'destination': 'Solar Observatory',
            'launch_date': '2024-03-30T00:00:00',
            'duration_days': 451,
            'crew': [
                {
                    'member_id': 'CM001',
                    'name': 'Sarah Williams',
                    'rank': 'captain',
                    'age': 43,
                    'specialization': 'Mission Command',
                    'years_experience': 19,
                    'is_active': True
                },
                {
                    'member_id': 'CM002',
                    'name': 'James Hernandez',
                    'rank': 'captain',
                    'age': 43,
                    'specialization': 'Pilot',
                    'years_experience': 30,
                    'is_active': True
                },
                {
                    'member_id': 'CM003',
                    'name': 'Anna Jones',
                    'rank': 'cadet',
                    'age': 35,
                    'specialization': 'Communications',
                    'years_experience': 15,
                    'is_active': True
                },
                {
                    'member_id': 'CM004',
                    'name': 'David Smith',
                    'rank': 'commander',
                    'age': 27,
                    'specialization': 'Security',
                    'years_experience': 15,
                    'is_active': True
                },
                {
                    'member_id': 'CM005',
                    'name': 'Maria Jones',
                    'rank': 'cadet',
                    'age': 55,
                    'specialization': 'Research',
                    'years_experience': 30,
                    'is_active': True
                }
            ],
            'mission_status': 'planned',
            'budget_millions': 2208.1
        },
        {
            'mission_id': 'M2024_MARS',
            'mission_name': 'Jupiter Orbit Colony Mission',
            'destination': 'Jupiter Orbit',
            'launch_date': '2024-10-01T00:00:00',
            'duration_days': 1065,
            'crew': [
                {
                    'member_id': 'CM011',
                    'name': 'Emma Brown',
                    'rank': 'commander',
                    'age': 49,
                    'specialization': 'Mission Command',
                    'years_experience': 27,
                    'is_active': True
                },
                {
                    'member_id': 'CM012',
                    'name': 'John Hernandez',
                    'rank': 'lieutenant',
                    'age': 36,
                    'specialization': 'Science Officer',
                    'years_experience': 22,
                    'is_active': True
                },
                {
                    'member_id': 'CM013',
                    'name': 'Sofia Rodriguez',
                    'rank': 'commander',
                    'age': 29,
                    'specialization': 'Life Support',
                    'years_experience': 20,
                    'is_active': True
                },
                {
                    'member_id': 'CM014',
                    'name': 'Sofia Lopez',
                    'rank': 'lieutenant',
                    'age': 44,
                    'specialization': 'Systems Analysis',
                    'years_experience': 25,
                    'is_active': True
                }
            ],
            'mission_status': 'planned',
            'budget_millions': 4626.0
        },
        {
            'mission_id': 'M2024_EUROPA',
            'mission_name': 'Europa Colony Mission',
            'destination': 'Europa',
            'launch_date': '2024-02-07T00:00:00',
            'duration_days': 666,
            'crew': [
                {
                    'member_id': 'CM021',
                    'name': 'Lisa Garcia',
                    'rank': 'captain',
                    'age': 36,
                    'specialization': 'Medical Officer',
                    'years_experience': 12,
                    'is_active': True
                },
                {
                    'member_id': 'CM022',
                    'name': 'John Garcia',
                    'rank': 'cadet',
                    'age': 46,
                    'specialization': 'Security',
                    'years_experience': 25,
                    'is_active': True
                },
                {
                    'member_id': 'CM023',
                    'name': 'Michael Johnson',
                    'rank': 'officer',
                    'age': 54,
                    'specialization': 'Research',
                    'years_experience': 30,
                    'is_active': True
                },
                {
                    'member_id': 'CM024',
                    'name': 'Sarah Rodriguez',
                    'rank': 'lieutenant',
                    'age': 54,
                    'specialization': 'Research',
                    'years_experience': 30,
                    'is_active': True
                },
                {
                    'member_id': 'CM025',
                    'name': 'Maria Smith',
                    'rank': 'cadet',
                    'age': 38,
                    'specialization': 'Communications',
                    'years_experience': 15,
                    'is_active': True
                }
            ],
            'mission_status': 'planned',
            'budget_millions': 4976.0
        },
        {
            'mission_id': 'M2024_LUNA',
            'mission_name': 'Mars Colony Mission',
            'destination': 'Mars',
            'launch_date': '2024-06-13T00:00:00',
            'duration_days': 222,
            'crew': [
                {
                    'member_id': 'CM031',
                    'name': 'Anna Davis',
                    'rank': 'commander',
                    'age': 27,
                    'specialization': 'Communications',
                    'years_experience': 14,
                    'is_active': True
                },
                {
                    'member_id': 'CM032',
                    'name': 'Elena Garcia',
                    'rank': 'lieutenant',
                    'age': 42,
                    'specialization': 'Science Officer',
                    'years_experience': 23,
                    'is_active': True
                },
                {
                    'member_id': 'CM033',
                    'name': 'Anna Brown',
                    'rank': 'officer',
                    'age': 55,
                    'specialization': 'Engineering',
                    'years_experience': 30,
                    'is_active': True
                },
                {
                    'member_id': 'CM034',
                    'name': 'Emma Smith',
                    'rank': 'captain',
                    'age': 37,
                    'specialization': 'Research',
                    'years_experience': 23,
                    'is_active': True
                },
                {
                    'member_id': 'CM035',
                    'name': 'Sofia Smith',
                    'rank': 'lieutenant',
                    'age': 53,
                    'specialization': 'Security',
                    'years_experience': 30,
                    'is_active': True
                },
                {
                    'member_id': 'CM036',
                    'name': 'Maria Hernandez',
                    'rank': 'commander',
                    'age': 41,
                    'specialization': 'Medical Officer',
                    'years_experience': 30,
                    'is_active': True
                },
                {
                    'member_id': 'CM037',
                    'name': 'John Hernandez',
                    'rank': 'officer',
                    'age': 42,
                    'specialization': 'Science Officer',
                    'years_experience': 20,
                    'is_active': True
                }
            ],
            'mission_status': 'planned',
            'budget_millions': 4984.6
        },
        {
            'mission_id': 'M2024_EUROPA',
            'mission_name': 'Saturn Rings Research Mission',
            'destination': 'Saturn Rings',
            'launch_date': '2024-09-18T00:00:00',
            'duration_days': 602,
            'crew': [
                {
                    'member_id': 'CM041',
                    'name': 'William Davis',
                    'rank': 'captain',
                    'age': 35,
                    'specialization': 'Medical Officer',
                    'years_experience': 14,
                    'is_active': True
                },
                {
                    'member_id': 'CM042',
                    'name': 'Sarah Smith',
                    'rank': 'captain',
                    'age': 55,
                    'specialization': 'Research',
                    'years_experience': 30,
                    'is_active': True
                },
                {
                    'member_id': 'CM043',
                    'name': 'Elena Garcia',
                    'rank': 'commander',
                    'age': 55,
                    'specialization': 'Research',
                    'years_experience': 30,
                    'is_active': True
                },
                {
                    'member_id': 'CM044',
                    'name': 'Sofia Williams',
                    'rank': 'officer',
                    'age': 30,
                    'specialization': 'Systems Analysis',
                    'years_experience': 9,
                    'is_active': True
                },
                {
                    'member_id': 'CM045',
                    'name': 'Sarah Jones',
                    'rank': 'lieutenant',
                    'age': 25,
                    'specialization': 'Maintenance',
                    'years_experience': 11,
                    'is_active': True
                },
                {
                    'member_id': 'CM046',
                    'name': 'Lisa Rodriguez',
                    'rank': 'officer',
                    'age': 30,
                    'specialization': 'Life Support',
                    'years_experience': 12,
                    'is_active': True
                },
                {
                    'member_id': 'CM047',
                    'name': 'Sarah Smith',
                    'rank': 'cadet',
                    'age': 28,
                    'specialization': 'Pilot',
                    'years_experience': 8,
                    'is_active': True
                }
            ],
            'mission_status': 'planned',
            'budget_millions': 1092.6
        }
    ]

    mission = random.choice(SPACE_MISSIONS)
    for i in range(len(mission['crew'])):
        memb = mission['crew'][i]
        mission['crew'][i] = CrewMember(**memb)
    space_mission = SpaceMission(**mission)

    print("Valid mission created:")
    print(f"Mission: {space_mission.mission_name}")
    print(f"ID: {space_mission.mission_id}")
    print(f"Destination: {space_mission.destination}")
    print(f"Duration: {space_mission.duration_days} days")
    print(f"Budget: ${space_mission.budget_millions}M")
    print(f"Crew size: {len(space_mission.crew)}")
    print("Crew members:")
    for member in space_mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - {member.specialization}")

    print("\n=========================================")
    print("Expected validation error:")
    try:
        invalid_mission: dict = {
            'mission_id': 'M2024_EUROPA',
            'mission_name': 'Saturn Rings Research Mission',
            'destination': 'Saturn Rings',
            'launch_date': '2024-09-18T00:00:00',
            'duration_days': 602,
            'crew': [
                CrewMember(
                    member_id="CM041",
                    name="William Davis",
                    rank=Rank.CADET,
                    age=35,
                    specialization="Medical Officer",
                    years_experience=14,
                    is_active=True,
                ),
                CrewMember(
                    member_id="CM042",
                    name="Alphonso Davis",
                    rank=Rank.OFFICER,
                    age=27,
                    specialization="Medical Officer",
                    years_experience=12,
                    is_active=True,
                ),
            ],
            'mission_status': 'planned',
            'budget_millions': 1092.6
        }
        SpaceMission(**invalid_mission)
    except ValidationError as e:
        err_msg: str = e.errors()[0]['msg']
        # Remove 'Value error' from error message
        if "Value error" in err_msg:
            err_msg = err_msg.replace("Value error, ", "")
        print(err_msg)


if __name__ == "__main__":
    main()
