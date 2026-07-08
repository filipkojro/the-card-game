from fastapi import FastAPI

from engine import cards_stack_number, create_game, notation_to_card
from models import Card, CardColor, CardGroup

gme = create_game(["bob", "alice"])

gme.desk.append(
    CardGroup(
        cards=[Card(value=4, color=CardColor.KARO, win_condition=False)],
    )
)


app = FastAPI()


@app.get("/")
async def root():
    card = notation_to_card(gme, "041")
    if card is not None:
        return cards_stack_number(gme, card)
    else:
        return "nieeeee"
