import uuid

from models import *

def gen_classic_card_color(color: CardColor) -> CardGroup:
    cards = []
    for i in range(2, 15):
        cards.append(Card(id=uuid.uuid4(), value=i, color=color, win_condition=i>10))
    return CardGroup(id=uuid.uuid4(), cards=cards)

def create_game(player_names: list[str]) -> GameState:
    assert len(player_names) <= 4

    colors = [c for c in CardColor]

    players = []

    for i, name in enumerate(player_names):
        players.append(Player(id=uuid.uuid4(), username=name, hand=gen_classic_card_color(color=colors[i])))

    return GameState(id=uuid.uuid4(), players=players, desk=[])