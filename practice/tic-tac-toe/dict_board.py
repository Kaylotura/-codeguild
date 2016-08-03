"""Class Module for Tic-Tac-Toe game that handles the board."""


class DictTTTBoard:
    """Creates a Board class as a dictionary of coordinates to tokens."""

    def __init__(self):
        r"""Initialize Class
        >>> a = DictTTTBoard()
        >>> sorted(a._coord_to_token)
        [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        """
        self._coord_to_token = {
            (0, 0): ' ',
            (1, 0): ' ',
            (2, 0): ' ',
            (0, 1): ' ',
            (1, 1): ' ',
            (2, 1): ' ',
            (0, 2): ' ',
            (1, 2): ' ',
            (2, 2): ' '
        }

    def __repr__(self):
        """Return representation.
        # concerned with how useless repr will be for human interpretation.

        >>> a = DictTTTBoard()
        >>> a._coord_to_token = {(0, 0): 'X'}
        >>> a
        DictTTTBoard({(0, 0): 'X'})
        """
        return 'DictTTTBoard({!r})'.format(self._coord_to_token)

    def __eq__(self, other):
        """Defines equality.

        >>> a = DictTTTBoard()
        >>> a._coord_to_token = {(0, 0): 'X'}
        >>> b = DictTTTBoard()
        >>> b._coord_to_token = {(0, 0): 'X'}
        >>> a == b
        True
        >>> a = DictTTTBoard()
        >>> a._coord_to_token = {(0, 0): 'X'}
        >>> b = DictTTTBoard()
        >>> b._coord_to_token = {(0, 1): 'X'}
        >>> a == b
        False
        """
        return self._coord_to_token == other._coord_to_token

    def place_token(self, x, y, token):
        """Place a token character string at a given coordinate.

        (top-left is 0, 0), x is horizontal position, y is vertical position

        >>> a = DictTTTBoard()
        >>> a._coord_to_token = {(0, 0): 'X'}
        >>> a.place_token(0, 1, 'O')
        >>> b = a._coord_to_token
        >>> sorted(b.items())
        [((0, 0), 'X'), ((0, 1), 'O')]
        >>> a = DictTTTBoard()
        >>> a._coord_to_token = {(0, 0): 'X', (0,1): 'O'}
        >>> a.place_token(0, 2, 'X')
        >>> b = a._coord_to_token
        >>> sorted(b.items())
        [((0, 0), 'X'), ((0, 1), 'O'), ((0, 2), 'X')]
        """
        self._coord_to_token[(x, y)] = token

    def make_rows(self):
        """Returns a list of listed tokens, in order of the rows going top down.

        >>> a = DictTTTBoard()
        >>> a._coord_to_token = {
        ...   (0,0): 'X', (1,0): ' ', (2,0): 'O',
        ...   (0,1): 'X', (1,1): 'O', (2,1): 'X',
        ...   (0,2): 'O', (1,2): ' ', (2,2): 'X'
        ...    }
        >>> a.make_rows()
        [['X', ' ', 'O'], ['X', 'O', 'X'], ['O', ' ', 'X']]
        """
        coords_to_tokens = sorted(list(self._coord_to_token.items()))
        return [[coord_to_token[1] for coord_to_token in coords_to_tokens
                 if coord_to_token[0][1] == x] for x in range(3)]

    def make_columns(self):
        """Returns a list of listed tokens, in order of the columns going left to right.

        >>> a = DictTTTBoard()
        >>> a._coord_to_token = {
        ...   (0,0): 'X', (1,0): ' ', (2,0): 'O',
        ...   (0,1): 'X', (1,1): 'O', (2,1): 'X',
        ...   (0,2): 'O', (1,2): ' ', (2,2): 'X'
        ...    }
        >>> a.make_columns()
        [['X', 'X', 'O'], [' ', 'O', ' '], ['O', 'X', 'X']]
        """
        coords_to_tokens = sorted(list(self._coord_to_token.items()))
        return [[coord_to_token[1] for coord_to_token in coords_to_tokens
                 if coord_to_token[0][0] == y] for y in range(3)]

    def make_diagonals(self):
        """Returns a list of listed tokens, in order of the diagonals left-down first, followed by left-up second.

        >>> a = DictTTTBoard()
        >>> a._coord_to_token = {
        ...   (0,0): 'X', (1,0): ' ', (2,0): 'O',
        ...   (0,1): 'X', (1,1): 'O', (2,1): 'X',
        ...   (0,2): 'O', (1,2): ' ', (2,2): 'X'
        ...    }
        >>> a.make_diagonals()
        [['X', 'O', 'X'], ['O', 'O', 'O']]
        """
        coords_to_tokens = sorted(list(self._coord_to_token.items()))
        diagonal_1 = [coord_to_token[1] for coord_to_token in coords_to_tokens
                      if coord_to_token[0][0] == coord_to_token[0][1]]
        diagonal_2 = [coord_to_token[1] for coord_to_token in coords_to_tokens
                      if sum([coord_to_token[0][0], coord_to_token[0][1]]) == 2]
        return [diagonal_1, diagonal_2]

    def calc_winner(self):
        """Determines what token string has won or returns None if no one has

        >>> a = DictTTTBoard()
        >>> a._coord_to_token = {}
        >>> a.calc_winner() == None
        True

        >>> a = DictTTTBoard()
        >>> a._coord_to_token = {
        ... (0, 0): 'X', (1, 0): 'X', (2, 0): '0',
        ... (0, 1): 'O', (1, 1): 'O', (2, 1): 'X',
        ... (0, 2): 'X', (1, 2): 'O', (2, 2): 'X'
        ... }
        >>> a.calc_winner() == None
        True


             >>> a = DictTTTBoard()
        >>> a._coord_to_token = {
        ... (0, 2): 'X', (1, 2): 'X', (2, 2): 'X'
        ... }
        >>> a.calc_winner()
        'X'

        >>> a = DictTTTBoard()
        >>> a._coord_to_token = {
        ... (2, 0): 'O',
        ... (2, 1): 'O',
        ... (2, 2): 'O'
        ... }
        >>> a.calc_winner()
        'O'

        >>> a = DictTTTBoard()
        >>> a._coord_to_token = {
        ... (0, 0): 'X', (2, 0): 'O',
        ... (1, 1): 'X',
        ... (2, 2): 'X'
        ... }
        >>> a.calc_winner()
        'X'
        """
        row_win_keys = self.make_rows()
        col_win_keys = self.make_columns()
        diag_win_keys = self.make_diagonals()
        all_win_keys = row_win_keys + col_win_keys + diag_win_keys

        if ['X', 'X', 'X'] in all_win_keys:
            return 'X'
        elif ['O', 'O', 'O'] in all_win_keys:
            return 'O'
        else:
            return None

    def __str__(self):
        r"""Returns a pretty-printed picture of the board.

        >>> a = DictTTTBoard()
        >>> a._coord_to_token = {
        ... (0,0): 'X', (1,0): 'X', (2,0): 'O',
        ... (0,1): 'O', (1,1): 'O', (2,1): 'X',
        ... (0,2): 'X', (1,2): ' ', (2,2): 'X'
        ... }
        >>> a.__str__()
        'X|X|O\nO|O|X\nX| |X\n'
        """
        rows = self.make_rows()
        pretty_rows = ['|'.join(row) for row in rows]
        return '\n'.join(pretty_rows) + '\n'
