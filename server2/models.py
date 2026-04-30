from pydantic import BaseModel
from enum import Enum
import uuid

class CardColor(Enum):
    KIER = 0
    KARO = 1
    TREFL = 2
    PIK = 3

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
    
    def check_card_on_top(self, card: Card) -> bool:
        for stack in self.desk:
            if card == stack.cards[-1]:
                return True
        return False