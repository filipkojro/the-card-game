from pydantic import BaseModel
from enum import StrEnum, auto
import uuid

class CardColor(StrEnum):
    KIER = auto()
    KARO = auto()
    TREFL = auto()
    PIK = auto()

class Card(BaseModel):
    id: uuid.UUID
    value: int
    color: CardColor
    win_condition: bool

class CardGroup(BaseModel):
    id: uuid.UUID
    cards: list[Card]

class Player(BaseModel):
    id: uuid.UUID
    username: str
    hand: CardGroup

class GameState(BaseModel):
    id: uuid.UUID
    players: list[Player]
    desk: list[CardGroup]