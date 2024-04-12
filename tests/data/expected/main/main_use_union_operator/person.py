# generated by datamodel-codegen:
#   filename:  person.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field, conint

from .definitions import food, friends
from .definitions.drink import coffee, tea
from .definitions.machine import robot
from .definitions.relative.animal.pet import pet


class Person(BaseModel):
    first_name: str = Field(..., description="The person's first name.")
    last_name: str = Field(..., description="The person's last name.")
    age: conint(ge=0) | None = Field(None, description='Age in years.')
    pets: List[pet.Pet] | None = None
    friends: friends.Friends | None = None
    robot: robot.Robot | None = None
    comment: None = None
    drink: List[coffee.Coffee | tea.Tea] | None = None
    food: List[food.Noodle | food.Soup] | None = None


Person.update_forward_refs()
