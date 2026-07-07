import uuid

from fastapi import FastAPI

from engine import create_game
from models import Card, CardColor, CardGroup

gme = create_game(["bob", "alice"])

gme.desk.append(
    CardGroup(
        id=uuid.uuid4(),
        cards=[
            Card(id=uuid.uuid4(), value=4, color=CardColor.KARO, win_condition=False)
        ],
    )
)


app = FastAPI()


@app.get("/")
async def root():
    return gme
