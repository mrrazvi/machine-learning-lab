import chess
import chess.svg

board = chess.Board()

print(board.legal_moves)
print(board.is_checkmate())

print(board)
