from games import *
class GameOfNim(Game):
    # YOUR CODE GOES HERE
    # raise NotImplementedError
     def __init__(self, board):
         moves=[]
         for x in range(len(board)):
            for y in range(1, board[x]+1):
                moves.append((x,y))
         self.initial = GameState(to_move='X', utility=0, board=board, moves=moves)
    
       
     def actions(self,state):
        # board=state.board
        # move=[]
        # for x in range(len(board)):
        #     for y in range(1, board[x]+1):
        #         move.append((x,y))
        # return move
         return state.moves



     def result(self,state,move):
       
        board=state.board
        moves = list(state.moves)
        board[move[0]] = board[move[0]] - move[1]
        moves=[]
        for x in range(len(board)):
            for y in range(1, board[x]+1):
                moves.append((x,y))

        return GameState(to_move=('O' if state.to_move == 'X' else 'X'),
                         utility=self.utility(state, state.to_move),
                         board=board, moves=moves)


     def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        return state.utility if player == 'X' else -state.utility


     def terminal_test(self, state):
        """A state is terminal if it is won or there are no empty squares."""
        return state.utility != 0 or len(state.moves) == 0


    
if __name__ == "__main__":
    
    nim = GameOfNim(board=[0, 5, 3, 1])  # Creating the game instance
    nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first
    if (utility < 0):
        print("MIN won the game")
        
    else:
        print("MAX won the game")