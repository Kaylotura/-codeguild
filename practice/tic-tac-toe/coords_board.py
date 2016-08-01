"""Class Module for Tic-Tac-Toe game that handles the board."""


class CoordsTTTBoard:
    """Creates a Board class to operate within."""

    def __init__(self):
        """Initialize Class
        >>> a = CoordsTTTBoard()
        >>> a
        CoordsTTTBoard([])
        """
        self._token_coords = []

    def __repr__(self):
        """Return representation.

        >>> a = CoordsTTTBoard()
        >>> a._token_coords  = [(1, 1, 'X'), (0, 1, 'O')]
        >>> a
        CoordsTTTBoard([(1, 1, 'X'), (0, 1, 'O')])
        """
        return 'CoordsTTTBoard({!r})'.format(self._token_coords)

    def __eq__(self, other):
        """Defines equality.

        >>> a = CoordsTTTBoard()
        >>> a._token_coords  = [(1, 1, 'X'), (0, 1, 'O')]
        >>> b = CoordsTTTBoard()
        >>> b._token_coords  = [(1, 1, 'X'), (0, 1, 'O')]
        >>> a == b
        True
        >>> a = CoordsTTTBoard()
        >>> a._token_coords  = [(1, 1, 'X'), (0, 1, 'O')]
        >>> b = CoordsTTTBoard()
        >>> b._token_coords  = [(2, 1, 'X'), (0, 1, 'O')]
        >>> a == b
        False
        """
        return self._token_coords == other._token_coords

    def place_token(self, x, y, token):
        """Place a token character string at a given coordinate.

        (top-left is 0, 0), x is horizontal position, y is vertical position

        >>> a = CoordsTTTBoard()
        >>> a._token_coords  = [(2, 1, 'X'), (0, 1, 'O')]
        >>> a.place_token(0, 0, 'O')
        >>> a
        CoordsTTTBoard([(2, 1, 'X'), (0, 1, 'O'), (0, 0, 'O')])
        """
        self._token_coords.append((x, y, token))

    def calc_winner(self):
        """Determines what token string has won or returns None if no one has

        >>> a = CoordsTTTBoard()
        >>> a._token_coords = []
        >>> a.calc_winner() == None
        True

        >>> a = CoordsTTTBoard()
        >>> a._token_coords = [
        ... (0, 0, 'X'), (1, 0, 'X'), (2, 0, 'O'),
        ... (0, 1, 'O'), (1, 1, 'O'), (2, 1, 'X'),
        ... (0, 2, 'X'), (1, 0, 'O'), (2, 2, 'X')
        ... ]
        >>> a.calc_winner() == None
        True

        >>> a = CoordsTTTBoard()
        >>> a._token_coords = [
        ... (0, 2, 'X'), (1, 2, 'X'), (2, 2, 'X')
        ... ]
        >>> a.calc_winner()
        'X'

        >>> a = CoordsTTTBoard()
        >>> a._token_coords = [
        ... (2, 0, 'O'),
        ... (2, 1, 'O'),
        ... (2, 2, 'O')
        ... ]
        >>> a.calc_winner()
        'O'

        >>> a = CoordsTTTBoard()
        >>> a._token_coords = [
        ... (0, 0, 'X'), (2, 0, 'O'),
        ... (1, 1, 'X'),
        ... (2, 2, 'X')
        ... ]
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

    def make_coords_to_tokens(self):
        return {(token_coord[0], token_coord[1]): token_coord[2]
                for token_coord in self._token_coords}

    def make_rows(self):
        """Returns a list of listed tokens, in order of the rows going top down.

        >>> a = CoordsTTTBoard()
        >>> a._token_coords = [
        ... (0, 0, 'X'), (1, 0, 'X'), (2, 0, 'O'),
        ... (0, 1, 'O'), (1, 1, 'O'), (2, 1, 'X'),
        ... (0, 2, 'X'), (2, 2, 'X')
        ... ]
        >>> a.make_rows()
        [['X', 'X', 'O'], ['O', 'O', 'X'], ['X', ' ', 'X']]
        """
        coords_to_tokens = self.make_coords_to_tokens()
        return [[coords_to_tokens.get((x, y), ' ') for x in range(3)]
                for y in range(3)]

    def make_columns(self):
        """Returns a list of listed tokens, in order of the columns going left to right.

        >>> a = CoordsTTTBoard()
        >>> a._token_coords = [
        ... (0, 0, 'X'), (1, 0, 'X'), (2, 0, 'O'),
        ... (0, 1, 'O'), (1, 1, 'O'), (2, 1, 'X'),
        ... (0, 2, 'X'), (2, 2, 'X')
        ... ]
        >>> a.make_columns()
        [['X', 'O', 'X'], ['X', 'O', ' '], ['O', 'X', 'X']]
        """
        coords_to_tokens = self.make_coords_to_tokens()
        return [[coords_to_tokens.get((x, y), ' ') for y in range(3)]
                for x in range(3)]

    def make_diagonals(self):
        """Returns a list of listed tokens, in order of the rows going top down.

        >>> a = CoordsTTTBoard()
        >>> a._token_coords = [
        ... (0, 0, 'X'), (1, 0, 'X'), (2, 0, 'O'),
        ... (0, 1, 'O'), (1, 1, 'O'), (2, 1, 'X'),
        ... (0, 2, 'X'), (2, 2, 'X')
        ... ]
        >>> a.make_diagonals()
        [['X', 'O', 'X'], ['X', 'O', 'O']]
        """
        coords_to_tokens = self.make_coords_to_tokens()
        diagonal_1 = [coords_to_tokens.get((0, 0), ' '), coords_to_tokens.get(
            (1, 1), ' '), coords_to_tokens.get((2, 2), ' ')]
        diagonal_2 = [coords_to_tokens.get((0, 2), ' '), coords_to_tokens.get(
            (1, 1), ' '), coords_to_tokens.get((2, 0), ' ')]
        return [diagonal_1, diagonal_2]

    def __str__(self):
        r"""Returns a pretty-printed picture of the Board .

        >>> a = CoordsTTTBoard()
        >>> a._token_coords = [
        ... (0, 0, 'X'), (1, 0, 'X'), (2, 0, 'O'),
        ... (0, 1, 'O'), (1, 1, 'O'), (2, 1, 'X'),
        ... (0, 2, 'X'), (2, 2, 'X')
        ... ]
        >>> a.__str__()
        'X|X|O\nO|O|X\nX| |X\n'
        """
        rows = self.make_rows()
        pretty_rows = ['|'.join(row) for row in rows]
        return '\n'.join(pretty_rows) + '\n'
