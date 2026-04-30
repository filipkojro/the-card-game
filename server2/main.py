from engine import *
from models import *

gme = create_game(["bob", "alice"])


for p in gme.players:
    print(p)