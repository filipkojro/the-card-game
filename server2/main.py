from fastapi import FastAPI

from engine import create_game
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
    return gme
