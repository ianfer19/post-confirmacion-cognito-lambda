from dataclasses import dataclass

@dataclass
class ConfirmedUser:
    sub: str
    email: str
    name: str
    birthdate: str
    gender: str
    phone_number: str
    confirmed_at: str
