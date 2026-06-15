try:
    from pydantic import BaseModel, Field, ValidationError, model_validator  # type: ignore  # noqa: E501
    from enum import Enum
    from datetime import datetime
except ModuleNotFoundError as err:
    print(f"Missing dependency: {err}")
    print("Create a virtual environment:")
    print("     python3 -m venv .venv")
    print("     source .venv/bin/activate")
    print("Install:")
    print("     pip install pydantic")
    exit()


class Rank(Enum):
    cadet = 'cadet'
    officer = 'officer'
    lieutenant = 'lieutenant'
    captain = 'captain'
    commander = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    # lista de modelos aninhados
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self) -> 'SpaceMission':
        # 01: ID da missao deve comecar com "M"
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        # 02: Deve ter pelo menos um Comandante ou Capitao
        ranks = [member.rank for member in self.crew]
        if Rank.captain not in ranks and Rank.commander not in ranks:
            raise ValueError('Mission must have at least one Commander or'
                             ' Captain')
        # 03: Missoes longas (> 365 dias) precisam de 50% de tripulacao
        # experiente (5+ anos)
        if self.duration_days > 365:
            total_crew = len(self.crew)
            experienced_count = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced_count += 1
            if experienced_count / total_crew < 0.5:
                raise ValueError('Long missions require at least 50% '
                                 'experienced crew (5+ years)')
        # 04: Todos os membros da tripulacao devem estar ativos
        for member in self.crew:
            if not member.is_active:
                raise ValueError(f'Crew member {member.name} is not active')
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    members = [
            {
                'member_id': '001',
                'name': 'Sarah Connor',
                'rank': 'commander',
                'age': '30',
                'specialization': 'Mission Command',
                'years_experience': 18,
                'is_active': True
            },
            {
                'member_id': '002',
                'name': 'John Smith',
                'rank': 'lieutenant',
                'age': '24',
                'specialization': 'Navigation',
                'years_experience': 1,
                'is_active': True
            },
            {
                'member_id': '004',
                'name': 'Alice Johnson',
                'rank': 'officer',
                'age': '39',
                'specialization': 'Engineering',
                'years_experience': 20,
                'is_active': True
            }
    ]

    member_valid = []

    for member in members:
        try:
            member_valid.append(CrewMember(**member))
        except ValidationError as exc:
            print("Expected validation error:")
            for error in exc.errors():
                if error['loc']:
                    for loc_error in error['loc']:
                        print(f"{loc_error} = {error['msg']}")
                else:
                    print(error['msg'])

    mission = {
            'mission_id': 'Mars Colony Establishment',
            'mission_name': 'M2024_MARS',
            'destination': 'Mars',
            'launch_date': '2024-01-15T10:00:00',
            'duration_days': 900,
            'crew': member_valid,
            'budget_millions': '9873.40'
    }
    try:
        mission_valid = (SpaceMission(**mission))
    except ValidationError as exc:
        print("Expected validation error:")
        for error in exc.errors():
            if error['loc']:
                for loc_error in error['loc']:
                    print(f"{loc_error} = {error['msg']}")
            else:
                print(error['msg'])
    else:
        print("Valid mission created:")
        print(f"Mission: {mission_valid.mission_name}")
        print(f"ID: {mission_valid.mission_id}")
        print(f"Destination: {mission_valid.destination}")
        print(f"Duration: {mission_valid.duration_days} days")
        print(f"Budget: ${mission_valid.budget_millions}M")
        print(f"Crew size: {len(mission_valid.crew)}")
        print("Crew members:")
        for member in mission_valid.crew:
            print(f"- {member.name} ({member.rank.value})"
                  f" - {member.specialization}")
        print("=========================================")


if __name__ == "__main__":
    main()
