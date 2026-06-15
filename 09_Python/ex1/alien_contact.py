try:
    from pydantic import BaseModel, Field, ValidationError, model_validator  # type: ignore  # noqa: E501
    from typing import Optional
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


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    # so aceita os valores definidos no Enum
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    # O decorador @model_validator permite validar o modelo inteiro apos todos
    # os campos terem sido validados.
    @model_validator(mode='after')
    def validator_contact(self) -> 'AlienContact':
        # 01: ID deve comecar com "AC" (Alien Contact)
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        # 02: Relatorios de contato fisico devem ser verificados
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError('Physical contact reports must be verified')

        # 03: Contato telepatico requer pelo menos 3 testemunhas
        if (self.contact_type == ContactType.telepathic
                and self.witness_count < 3):
            raise ValueError('Telepathic contact requires at least'
                             '3 witnesses')

        # 04: Sinais fortes (> 7.0) devem incluir mensagens recebidas
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError('Strong signals must include received messages')

        # OBRIGATORIO retornar self
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    valid = {
            'contact_id': 'AC_2024_001',
            'timestamp': '2024-01-15T10:00:00',
            'location': 'Area 51, Nevada',
            'contact_type': 'radio',
            'signal_strength': 8.5,
            'duration_minutes': 45,
            'witness_count': 5,
            'message_received': 'Greetings from Zeta Reticuli',
            'is_verified': True
    }
    # crio um dicinario para as informacoes validas
    invalid = {
            'contact_id': 'AC_2024_002',
            'timestamp': '2024-02-15T10:00:00',
            'location': 'Area 51, Nevada',
            'contact_type': 'telepathic',
            'signal_strength': 8.5,
            'duration_minutes': 45,
            'witness_count': 2,
            'message_received': 'Greetings from Zeta Reticuli'
    }
    # crio uma lista para interar sobre os dicionarios/informacoes
    datas = [valid, invalid]

    for data in datas:
        try:
            contact = AlienContact(**data)
        except ValidationError as exc:
            print("Expected validation error:")
            for error in exc.errors():
                if error['loc']:
                    for loc_error in error['loc']:
                        print(f"{loc_error} = {error['msg']}")
                else:
                    print(error['msg'])
        else:
            print("========================================")
            print("Valid contact report:")
            print("ID:", contact.contact_id)
            print("Type:", contact.value)
            print("Location:", contact.location)
            print(f"Signal: {contact.signal_strength}/10")
            print(f"Duration: {contact.duration_minutes} minutes")
            print(f"Witnesses: {contact.witness_count}")
            print(f"Message: '{contact.message_received}'")
            print("========================================")


if __name__ == "__main__":
    main()
