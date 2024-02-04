def winner(moves, pc_move_index, user_move_index):
    if pc_move_index == user_move_index:
        return "Draw"
    ordered_moves = moves[pc_move_index:] + moves[:pc_move_index]
    new_user_index = ordered_moves.index(moves[user_move_index])
    if new_user_index < len(ordered_moves) / 2:
        return 'You win'
    return 'PC wins'
