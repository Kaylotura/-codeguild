"""Class Module for Tic-Tac-Toe game that handles the board."""


class DictTTTBoard:
    """Creates a Board class as a dictionary of coordinates to tokens."""
    def __init__(self):
        """Initialize Class
        >>> a = DictTTTBoard()
        >>> a
        DictTTTBoard({})
        """
        self._coord_to_token = {}

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
        return (
            self._coord_to_token == other._coord_to_token
        )

    def place_token(self, x, y, token):
        """Place a token character string at a given coordinate.

        (top-left is 0, 0), x is horizontal position, y is vertical position

        >>> a = DictTTTBoard()
        >>> a._coord_to_token = {(0, 0): 'X'}
        >>> a.place_token(0, 1, 'O')
        >>> a
        DictTTTBoard({(0, 0): 'X', (0, 1): 'O'})
        >>> a = DictTTTBoard()
        >>> a._coord_to_token = {(0, 0): 'X', (0,1): 'O'}
        >>> a.place_token(0, 2, 'X')
        >>> a
        DictTTTBoard({(0, 0): 'X', (0, 1): 'O', (0, 2): 'X'})
        """
        self._coord_to_token[(x, y)] = token

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

        WIN_LINES = [(self._middle_row[0], self._middle_row[1], self._middle_row[2]),
                     (self._top_row[1], self._middle_row[1], self._bottom_row[1]),
                     (self._top_row[0], self._middle_row[1], self._bottom_row[2]),
                     (self._top_row[2], self._middle_row[1], self._bottom_row[0]),
                     (self._top_row[0], self._top_row[1], self._top_row[2]),
                     (self._top_row[0], self._middle_row[0], self._bottom_row[0]),
                     (self._bottom_row[0], self._bottom_row[1], self._bottom_row[2]),
                     (self._top_row[2], self._middle_row[2], self._bottom_row[2])
                     ]

        if ('X', 'X', 'X') in WIN_LINES:
            return 'X'
        elif ('O', 'O', 'O') in WIN_LINES:
            return 'O'
        else:
            return None

    def __str__(self):
        """Returns a pretty-printed picture of the board.

        >>> a = DictTTTBoard()
        >>> a._coord_to_token = { = ['X', 'X', 'O']
        >>> a._middle_row = ['O', 'O', 'X']
        >>> a._bottom_row = ['X', ' ', 'X']
        >>> a.__str__()
        X|X|O
        O|O|X
        X| |X
        """
        return self._top_row[0] + '|' + self._top_row[1] + '|' + self._top_row[2]
        self._middle_row[0] + '|' + self._middle_row[1] + '|' + self._middle_row[2])
        self._bottom_row[0] + '|' + self._bottom_row[1] + '|' + self._bottom_row[2])



        """
        cell01 = ' '
        cell02 = ' '
        cell10 = ' '
        cell11 = ' '
        cell12 = ' '
        cell20 = ' '
        cell21 = ' '
        cell22 = ' '

        self._token_coords
        self._token_coords

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
