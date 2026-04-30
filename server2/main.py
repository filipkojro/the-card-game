import uuid

from engine import *
from models import *

gme = create_game(["bob", "alice"])

gme.desk.append(CardGroup(id=uuid.uuid4(), cards=[Card(id=uuid.uuid4(), value=4, color=CardColor.KARO, win_condition=False)]))

print(gme.state_str())