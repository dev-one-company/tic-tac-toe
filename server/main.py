from repository import Board

from flask import Flask, request

app = Flask(__name__)


@app.route('/start', methods=['POST'])
def start():
    board = Board.Board()
    board_id = board.create()

    if board_id is not None:
        return {
                   'board_id': board_id
               }, 201

    return {
               'message': "cannot create the board"
           }, 500


@app.route('/board/<board_id>', methods=['GET'])
def get_board(board_id: str):
    board = Board.Board()

    try:
        data = board.get_board(board_id)

        return {
            'data': data
        }, 200
    except Exception as e:
        return {
            'message': str(e)
        }, 500


@app.route('/mark_board_position', methods=['POST'])
def mark_board_position():
    body = request.json

    try:
        t_row = str(body['row'])
        t_column = str(body['column'])
        t_player = str(body['player'])

        if not t_row.isnumeric():
            return {
                       'message': "the param 'row' must be a integer"
                   }, 400
        if not t_column.isnumeric():
            return {
                       'message': "the param 'column' must be a integer"
                   }, 400
        if not t_player.isnumeric():
            return {
                       'message': "the param 'player' must be a integer"
                   }, 400

        if t_player not in ['1', '0']:
            return {
                       'message': "the player must be '1' or '0'"
                   }, 400

        row = int(t_row)
        column = int(t_column)
        player = int(t_player)
        board_id = str(body['board_id'])
    except KeyError:
        return {
                   'message': "please inform: 'row', 'column', 'player']"
               }, 400

    board = Board.Board()

    try:
        board.mark_board_position(row, column, board_id, player)
        return {
                   'message': "marked"
               }, 201
    except Exception as e:
        return {
                   'message': str(e)
               }, 400
