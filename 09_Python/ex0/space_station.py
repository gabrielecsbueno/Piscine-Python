try:
    from pydantic import BaseModel, Field, ValidationError  # type: ignore
    from typing import Optional
    from datetime import datetime
except ModuleNotFoundError as err:
    print(f"Missing dependency: {err}")
    print("Create a virtual environment:")
    print("     python3 -m venv .venv")
    print("     source .venv/bin/activate")
    print("Install:")
    print("     pip install pydantic")
    exit()


class SpaceStation(BaseModel):
    # Strings: min_length e max_length
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    # Numeros: ge (>=), le (<=), gt (>), lt (<)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    # Com valor padrao
    is_operational: bool = True
    # Campo opcional com max (default - valor padrao)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")

    # crio um dicinario para as informacoes validas
    valid = {
            'station_id': 'ISS001',
            'name': 'International Space Station',
            'crew_size': 6,
            'power_level': 85.5,
            'oxygen_level': 92.3,
            'last_maintenance': '2024-01-15T10:00:00'
    }
    # crio um dicinario para as informacoes validas
    invalid = {
            'station_id': 'ISS001',
            'name': 'International Space Station',
            'crew_size': 21,
            'power_level': 85.5,
            'oxygen_level': 92.3,
            'last_maintenance': '2024-01-15T10:00:00'
    }
    # crio uma lista para interar sobre os dicionarios/informacoes
    datas = [valid, invalid]

    for data in datas:
        try:
            # desempacotamento de dicionário com **
            station = SpaceStation(**data)
        except ValidationError as exc:
            print("Expected validation error:")
            for error in exc.errors():
                msg_error = error['msg']
                for loc_error in error['loc']:
                    print(f"{loc_error} = {msg_error}")
        else:
            print("========================================")
            print("Valid station created:")
            print("ID:", station.station_id)
            print("Name:", station.name)
            print(f"Crew: {station.crew_size} people")
            print(f"Power: {station.power_level}%")
            print(f"Oxygen: {station.oxygen_level}%")
            st = 'Operational' if station.is_operational else 'Not Operational'
            print(f"Status: {st}")
            print("========================================")


if __name__ == "__main__":
    main()
