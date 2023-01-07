def find_moves(checkers, dice1, dice2):
    possible_moves = []
    important_doors = {5, 6, 7, 8, 17, 18, 19, 20}
    for start_pos, num_checkers in checkers.items():
        for dice in (dice1, dice2):
            end_pos = start_pos + dice
            if end_pos in checkers:
                if checkers[end_pos] <= 1:
                    score = 0
                    if end_pos in important_doors:
                        score += 2
                    else:
                        score += 1
                    score -= 1
                    possible_moves.append(((start_pos, end_pos), score))
            else:
                score = 0
                if end_pos in important_doors:
                    score -= 2
                else:
                    score -= 1
                score += 1
                possible_moves.append(((start_pos, end_pos), score))
    return possible_moves

print(find_moves(checkers, 6, 1))
