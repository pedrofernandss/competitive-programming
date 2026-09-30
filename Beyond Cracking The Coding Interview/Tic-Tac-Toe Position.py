def gameHasBeenWon(game: list[list[int]], current_value: str) -> bool:

    # Check row
    for row in game:
        elements_required = len(game)
        for element in row:
            if element == current_value:
                elements_required -= 1
            else:
                break
    
        if elements_required == 0:
            return True


    # Check column
    for column in range(len(game)):
        elements_required = len(game)
        for row in range(len(game)):
            if game[row][column] == current_value:
                elements_required -= 1
            else:
                break

        if elements_required == 0:
            return True

    # Check first diagonal
    elements_required = len(game)
    for current_idx in range(len(game)):
        if game[current_idx][current_idx] == current_value:
            elements_required -= 1
        else:
            break
    
    if elements_required == 0:
        return True
    
    # Check second diagonal
    elements_required = len(game)
    for current_idx in range(len(game)-1, -1, -1): 
        if game[current_idx][len(game)-1-(current_idx)] == current_value:
            elements_required -= 1
        else:
            break
    
    if elements_required == 0:
            return True
    
    return False

def validTicTacToe(game: list[list[int]]) -> bool:
    countX = 0
    countO = 0
    
    for row_idx in range(len(game)):
        for column_idx in range(len(game[row_idx])):
            if game[row_idx][column_idx] == 'X':
                countX += 1
            elif game[row_idx][column_idx] == 'O':
                countO += 1
 
    gameIsWonByX = gameHasBeenWon(game, 'X')
    gameIsWonByO = gameHasBeenWon(game, 'O')

    if (gameIsWonByX and countO+1 == countX) or ((gameIsWonByO and not gameIsWonByX) and countO == countX) or (countO == countX and (not gameIsWonByO and not gameIsWonByX)) or (countO+1 == countX and not gameIsWonByO) or (countO+1 == countX and (not gameIsWonByO and not gameIsWonByX)):
        return True
    
    return False
