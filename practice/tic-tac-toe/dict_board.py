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
        win_keys = [
            [self._coord_to_token.get((1, 0), ' '), self._coord_to_token.get((1, 1), ' '),
             self._coord_to_token.get((1, 2), ' ')],

            [self._coord_to_token.get((0, 1), ' '), self._coord_to_token.get((1, 1), ' '),
             self._coord_to_token.get((2, 1), ' ')],

            [self._coord_to_token.get((0, 2), ' '), self._coord_to_token.get((1, 1), ' '),
             self._coord_to_token.get((2, 0), ' ')],

            [self._coord_to_token.get((0, 0), ' '), self._coord_to_token.get((1, 1), ' '),
             self._coord_to_token.get((2, 2), ' ')],

            [self._coord_to_token.get((0, 0), ' '), self._coord_to_token.get((1, 2), ' '),
             self._coord_to_token.get((0, 2), ' ')],

            [self._coord_to_token.get((0, 0), ' '), self._coord_to_token.get((0, 1), ' '),
             self._coord_to_token.get((0, 2), ' ')],

            [self._coord_to_token.get((2, 2), ' '), self._coord_to_token.get((2, 1), ' '),
             self._coord_to_token.get((2, 0), ' ')],

            [self._coord_to_token.get((2, 2), ' '), self._coord_to_token.get((1, 2), ' '),
             self._coord_to_token.get((0, 2), ' ')]
        ]

        if ['X', 'X', 'X'] in win_keys:
            return 'X'
        elif ['O', 'O', 'O'] in win_keys:
            return 'O'
        else:
            return None

    def __str__(self):
        r"""Returns a pretty-printed picture of the board.

        >>> a = DictTTTBoard()
        >>> a._coord_to_token = {
        ... (0,0): 'X', (1,0): 'X', (2,0): 'O',
        ... (0,1): 'O', (1,1): 'O', (2,1): 'X',
        ... (0,2): 'X', (2,2): 'X'
        ... }
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
        self._coord_to_token.items()
        for pair in list(self._coord_to_token.items()):
            if pair[0] == (0, 0):
                cell00 = pair[1]
            if pair[0] == (0, 1):
                cell01 = pair[1]
            if pair[0] == (0, 2):
                cell02 = pair[1]
            if pair[0] == (1, 0):
                cell10 = pair[1]
            if pair[0] == (1, 1):
                cell11 = pair[1]
            if pair[0] == (1, 2):
                cell12 = pair[1]
            if pair[0] == (2, 0):
                cell20 = pair[1]
            if pair[0] == (2, 1):
                cell21 = pair[1]
            if pair[0] == (2, 2):
                cell22 = pair[1]
        return cell00 + '|' + cell10 + '|' + cell20 + '\n' +\
            cell01 + '|' + cell11 + '|' + cell21 + '\n' +\
            cell02 + '|' + cell12 + '|' + cell22
