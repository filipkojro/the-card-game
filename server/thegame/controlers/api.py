from fastapi import APIRouter, WebSocket

from ..models.cards import State, Move

router = APIRouter()


CURRENT_STATE =  State(common_card_groups=[], player_cards=[], other_players=[], current_player_id=1)
LISTENERS: list[WebSocket] = []


@router.get("/state")
async def get_state() -> State:
    return CURRENT_STATE

@router.post("/make_move")
async def make_move(move: Move) -> State:
    for socket in LISTENERS:
        try:
            await socket.send_json(CURRENT_STATE)
        except Exception as e:
            print(e)
            LISTENERS.remove(socket)
    return CURRENT_STATE

@router.websocket("/subscribe")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json(CURRENT_STATE)
    LISTENERS.append(websocket)
    # while True:
    #     data = await websocket.receive_text()
    #     print(data)
    #     await websocket.send_text(data)