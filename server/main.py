from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from enum import StrEnum, auto

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

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
    player_cards: list[Card]
    current_player_id: int

class Move(BaseModel):
    card_ids: list[int]
    group_id: int

CURRENT_STATE =  State(common_card_groups=[], player_cards=[], other_players=[], current_player_id=1)
LISTENERS: list[WebSocket] = []

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.get("/state")
async def get_state() -> State:
    return CURRENT_STATE

@app.post("/make_move")
async def make_move(move: Move) -> State:
    for socket in LISTENERS:
        try:
            await socket.send_json(CURRENT_STATE)
        except Exception as e:
            LISTENERS.remove(socket)
    return CURRENT_STATE

@app.websocket("/subscribe")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json(CURRENT_STATE)
    LISTENERS.append(websocket)
    # while True:
    #     data = await websocket.receive_text()
    #     print(data)
    #     await websocket.send_text(data)