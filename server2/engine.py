import uuid

from models import Card, CardColor, CardGroup, GameState, Player


def gen_classic_card_color(color: CardColor) -> CardGroup:
    cards = []
    for i in range(2, 15):
        cards.append(Card(id=uuid.uuid4(), value=i, color=color, win_condition=i > 10))
    return CardGroup(id=uuid.uuid4(), cards=cards)


def create_game(player_names: list[str]) -> GameState:
    assert len(player_names) <= 4

    colors = [c for c in CardColor]

    players = []

    for i, name in enumerate(player_names):
        players.append(
            Player(
                id=uuid.uuid4(),
                username=name,
                hand=gen_classic_card_color(color=colors[i]),
            )
        )

    return GameState(id=uuid.uuid4(), players=players, desk=[])


def notation_to_card(game_state: GameState, card: str) -> Card | None:
    if len(card) != 3:
        return None

    card_value = int(card[:2])
    card_color = int(card[2])

    for stack in game_state.desk:
        for c in stack.cards:
            if c.value == card_value and c.color.value == card_color:
                return c
    return None


def check_card_on_top(game_state: GameState, card: Card) -> bool:
    for stack in game_state.desk:
        if card == stack.cards[-1]:
            return True
    return False


def check_group_on_top(game_state: GameState, bottom_card: Card) -> bool:
    for stack in game_state.desk:
        last_card = stack.cards[-1]
        for card in reversed(stack.cards):
            if card.color != last_card.color or card.value > last_card.value:
                continue
            if card == bottom_card:
                return True
            last_card = card
    return False


def group_value(game_state: GameState, bottom_card: Card) -> int:
    for stack in game_state.desk:
        value = 0
        last_card = stack.cards[-1]
        for card in reversed(stack.cards):
            if (
                card.color != last_card.color or card.value > last_card.value
            ):  # if bottom_card is last in gropu i think something break
                value = 0
            value += card.value
            if card == bottom_card:
                return value
            last_card = card
    return 0


def group_bottom_card(game_state: GameState, any_card: Card) -> Card | None:
    for stack in game_state.desk:
        found_group = False
        last_card = stack.cards[-1]
        for card in reversed(stack.cards):
            if (
                card.color != last_card.color or card.value > last_card.value
            ):  # if bottom_card is last in gropu i think something break
                if found_group:
                    return last_card
            if card == any_card:
                found_group = True
    return None


def make_move(game_state: GameState, src: str, dest: str) -> bool:
    src_card = notation_to_card(game_state, src)
    dest_card = notation_to_card(game_state, dest)

    if src_card is not None and not check_group_on_top(game_state, src_card):
        return False
    if dest_card is not None and not check_card_on_top(game_state, dest_card):
        return False
    return True
