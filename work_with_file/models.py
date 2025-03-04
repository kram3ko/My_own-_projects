import hashlib
from typing import Annotated, ClassVar
from pydantic import BaseModel, Field, field_validator


class User(BaseModel):
    last_id: ClassVar[int] = 0

    id_: Annotated[int, Field()]
    user_name: Annotated[str, Field(min_length=3, max_length=20)]
    password: Annotated[str, Field(min_length=8)]
    age: Annotated[int, Field(ge=1, le=100)]
    first_name: Annotated[str, Field(min_length=1, max_length=50)]
    last_name: Annotated[str, Field(min_length=1, max_length=50)]

    @field_validator("first_name", "last_name")
    @classmethod
    def auto_capitalize(cls, value: str):
        return value.capitalize()

    @field_validator("password")
    @classmethod
    def has_password(cls, value) -> str:
        return hashlib.sha256(value.encode()).hexdigest()

    def to_row(self):
        return (f"{self.id_} | {self.user_name} | {self.password} | "
                f"{self.age} | {self.first_name} | {self.last_name}\n")

    @classmethod
    def from_row(cls, row: str):
        id_, user_name, password, age, first_name, last_name = row.strip().split(" | ")
        return cls(
            id_=int(id_),
            user_name=user_name,
            password=password,
            age=int(age),
            first_name=first_name,
            last_name=last_name
        )
