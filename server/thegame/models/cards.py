from enum import StrEnum, auto
from pydantic import BaseModel

class CardColor(StrEnum):
    KIER = auto()
    KARO = auto()
    TREFL = auto()
    PIK = auto()

class Player(BaseModel):
    id: int
    username: str
    color: CardColor

class Card(BaseModel):
    id: int
    color: CardColor
    level: int

class CardGroup(BaseModel):
    group_id: int
    cards: list[Card]

class State(BaseModel):
    common_card_groups: list[CardGroup]
    other_players: list[Player]
    player_cards: list[CardGroup]
    current_player_id: int

    def all_card_groups(self):
        return self.player_cards + self.common_card_groups

    def card_group_by_id(self, group_id):
        for card_group in self.all_card_groups():
            if card_group.group_id == group_id:
                return card_group
        return None

class Move(BaseModel):
    card_ids: list[int]
    group_id: int
