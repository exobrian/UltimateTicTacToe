class GameBoard:
    def __init__(self):   
        #Create nine 3x3 boards. Each inner square is indexed by its ordinal number.
        board = [
            [[None]*3, [None]*3, [None]*3],
            [[None]*3, [None]*3, [None]*3],
            [[None]*3, [None]*3, [None]*3],
            [[None]*3, [None]*3, [None]*3],
            [[None]*3, [None]*3, [None]*3],
            [[None]*3, [None]*3, [None]*3],
            [[None]*3, [None]*3, [None]*3],
            [[None]*3, [None]*3, [None]*3],
            [[None]*3, [None]*3, [None]*3]
        ]
    
    def check_entry(self, inner_square_index, inner_move_index, game_board):
        #print(game_board.board)
        print("It worked")
        return None