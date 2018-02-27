# The ID_Improved agent is using alpha-beta pruning with iterative deepening
# and the improved heuristic function from the lecture. This provides a baseline
# performance with which we can compare our custom-designed heuristic function with.
# The tournament script runs the ID_Improved agent and the Student agent against a
# variety of different opponents.

# Random is random
# MM_Null uses the null evaluation function and minimax
# MM_Open uses the open moves evaluation function and minimax
# MM_Improved uses the improved evaluation function.
# The AB agent are the same but they use the alpha-beta algorithm and
# therefore can search deeper in the tree.
# Also note that all of these agents are used fixed-depth minimax and alphabeta.

player1 = CustomPlayer()
player2 = HumanPlayer()
player3 = GreedyPlayer()
player4 = RandomPlayer()

game = Board(player1, player4)

# Print board
print(Board.to_string(game))

# Moves are (rows, cols) starting with 0 indexing.
game.apply_move((2, 3))
game.apply_move((0, 5))
print(game.to_string())

game.active_player
game.get_legal_moves()
game.apply_move((0, 2))
game.apply_move((1, 3))

player1.minimax(game, 5)
# Not really sure how to get a predicted move from CustomPlayer.
# player1.get_move(game, game.get_legal_moves(), lambda: 10)

test = [(2,3), (1,2), (4,1)]
move = [(2,3), (1,2)]

# Play a game with Custom and Random.
winner, history, outcome = game.play()


board2 = Board(player1, player2)

board2.active_player

board2.active_player.get_move()

# Is a position good if the active player is in the center?
# Or if the player is able to move to the center
# If I had some kind of training set I think I could optimize the weights of the custom
# score function. The idea would be to get some labeled training data, with the labeling
# being whether particular move was the correct move or not. We could then run a regression
# where we minimize the MSE error between the predicted moves from our agent and the correct
# labeled moves.

# We want to evaluate the state of the board from the active player? A board where the
# active player is in the center of the board is good.
# num = 0
# for move in legal_moves:
#     if move in center:
#         num = num + 1
# return num



# Example player classes
# 1. null_score()
# 2. open_move_score()
# 3. improved_score()

# 1. RandomPlayer()
# 2. GreedyPlayer()
# 3. HumanPlayer()


# Board Class Methods
# 1. active_player()
# 2. inactive_player()
# 3. get_opponent()
# 4. copy()
# 5. forecast_move()
# 6. move_is_legal()
# 7. get_blank_spaces()
# 8. get_player_locations()
# 9. get_legal_moves()
# 10. apply_move()
# 11. is_winner()
# 12. is_loser()
# 13. utility()
# 14. __get_moves__()
# 15. print_board()
# 16. to_string()
# 17. play()


