import uuid
from enum import Enum

from pydantic import BaseModel


class CardColor(Enum):
    KIER = 0
    KARO = 1
    TREFL = 2
    PIK = 3


class Card(BaseModel):
    value: int
    color: CardColor
    win_condition: bool


class CardGroup(BaseModel):
    cards: list[Card]


class Player(BaseModel):
    player_id: uuid.UUID
    username: str
    hand: CardGroup


class GameState(BaseModel):
    game_id: uuid.UUID
    players: list[Player]
    desk: list[CardGroup]

    def state_str(self) -> str:
        state_str = ""
        for i in range(52):
            for group in self.desk:
                if len(group.cards) > i:
                    card = group.cards[i]
                    if card.value < 10:
                        value_str = f"0{card.value}"
                    else:
                        value_str = f"{card.value}"

                    state_str = state_str + value_str + f"{card.color.value}"
        return state_str
