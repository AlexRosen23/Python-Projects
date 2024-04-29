# tic_tac_toe_blocker.py

def tic_tac_toe_blocker(pos1, pos2):
    """
    This function returns the position on a tic-tac-toe board that blocks the player
    from winning based on two given positions.
    
    Parameters:
    pos1 (int): The first position marked by the player (0-8).
    pos2 (int): The second position marked by the player (0-8).
    
    Returns:
    int: The blocking position on the board, or -1 if no single block is possible.
    """
    # Mapping of indices to board positions:
    # 0 | 1 | 2
    # ---------
    # 3 | 4 | 5
    # ---------
    # 6 | 7 | 8
    
    # All possible winning combinations in tic-tac-toe
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal lines
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical lines
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    
    # Check each winning combination
    for combination in winning_combinations:
        if pos1 in combination and pos2 in combination:
            # Find the blocking position which is not already occupied by pos1 or pos2
            for position in combination:
                if position != pos1 and position != pos2:
                    return position
    # If there is no direct blocking move possible, return -1
    return -1

# Example usage: 
# print(tic_tac_toe_blocker(0, 1)) should return 2 as the blocking move.
