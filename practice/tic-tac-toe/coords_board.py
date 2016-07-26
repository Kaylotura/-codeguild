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
        return (
            self._token_coords == other._token_coords
        )

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
        win_coords = [
            [item[2] for item in self._token_coords if item[0] == 0],
            [item[2] for item in self._token_coords if item[0] == 1],
            [item[2] for item in self._token_coords if item[0] == 2],
            [item[2] for item in self._token_coords if item[1] == 0],
            [item[2] for item in self._token_coords if item[1] == 1],
            [item[2] for item in self._token_coords if item[1] == 0],
            [item[2] for item in self._token_coords if item[1] == 1],
            [item[2] for item in self._token_coords if item[1] == 2],
            [item[2] for item in self._token_coords if
                (item[0] == 0 and item[1] == 2) or
                (item[0] == 1 and item[1] == 1) or
                (item[0] == 2 and item[1] == 0)],
            [item[2] for item in self._token_coords if
                (item[0] == 0 and item[1] == 0) or
                (item[0] == 1 and item[1] == 1) or
                (item[0] == 2 and item[1] == 2)]
        ]
        if ['X', 'X', 'X'] in win_coords:
            return 'X'
        elif ['O', 'O', 'O'] in win_coords:
            return 'O'
        else:
            return None

    def __str__(self):
        r"""Returns a pretty-printed picture of the Board .

        >>> a = CoordsTTTBoard()
        >>> a._token_coords= [
        ... (0, 0, 'X'), (1, 0, 'X'), (2, 0, 'O'),
        ... (0, 1, 'O'), (1, 1, 'O'), (2, 1, 'X'),
        ... (0, 2, 'X'), (2, 2, 'X')
        ... ]
        >>> a.__str__()
        'X|X|O\nO|O|X\nX| |X'
        """
        cell00 = ' '
        cell01 = ' '
        cell02 = ' '
        cell10 = ' '
        cell11 = ' '
        cell12 = ' '
        cell20 = ' '
        cell21 = ' '
        cell22 = ' '
        for coord in self._token_coords:
            if coord[0] == 0 and coord[1] == 0:
                cell00 = coord[2]
            if coord[0] == 0 and coord[1] == 1:
                cell01 = coord[2]
            if coord[0] == 0 and coord[1] == 2:
                cell02 = coord[2]
            if coord[0] == 1 and coord[1] == 0:
                cell10 = coord[2]
            if coord[0] == 1 and coord[1] == 1:
                cell11 = coord[2]
            if coord[0] == 1 and coord[1] == 2:
                cell12 = coord[2]
            if coord[0] == 2 and coord[1] == 0:
                cell20 = coord[2]
            if coord[0] == 2 and coord[1] == 1:
                cell21 = coord[2]
            if coord[0] == 2 and coord[1] == 2:
                cell22 = coord[2]
        return cell00 + '|' + cell10 + '|' + cell20 + '\n' +\
            cell01 + '|' + cell11 + '|' + cell21 + '\n' +\
            cell02 + '|' + cell12 + '|' + cell22
