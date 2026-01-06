import chess
import chess.svg

board = chess.Board()

print(board.legal_moves)
print(board.is_checkmate())

board.push_san('e4')
board.push_san('e5')

print(board)
