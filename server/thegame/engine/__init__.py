from ..models.cards import Card, State, CardGroup,  Player

def make_move(state: State, card: Card, to_group: CardGroup, player: Player) -> State:
    assert state.current_player_id == player.id, "Wrong player trying to make a move"
    
    target_group = state.card_group_by_id(to_group.group_id)
    assert target_group is not None
    target_group.cards.append(card)

    for card_group in state.all_card_groups():
        if card in card_group.cards:
            card_group.cards.remove(card)
            return state
            
    raise RuntimeError("Player does not have the card they want to move")