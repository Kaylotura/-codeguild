"""Class Module for Tic-Tac-Toe game that handles the board."""


class Board:
    """Creates a Board class to operate within."""
    def __init__(self):
        """Initialize Class
        >>> a = Board()
        >>> a
        Board(['', '', ''], ['', '', ''], ['', '', ''])
        """
        self._top_row = ['', '', '']
        self._middle_row = ['', '', '']
        self._bottom_row = ['', '', '']

    def __repr__(self):
        """Return representation.

        >>> a = Board()
        >>> a._top_row = ['', 'X', 'O']
        >>> a
        Board(['', 'X', 'O'], ['', '', ''], ['', '', ''])
        """
        return 'Board({!r}, {!r}, {!r})'.format(self._top_row, self._middle_row, self._bottom_row)

    def __eq__(self, other):
        """Defines equality.

        >>> a = Board()
        >>> a._top_row = ['', 'X', 'O']
        >>> b = Board()
        >>> b._top_row = ['', 'X', 'O']
        >>> a == b
        True
        >>> a = Board()
        >>> a._top_row = ['', 'X', 'O']
        >>> b = Board()
        >>> b._top_row = ['X', 'O', 'O']
        >>> a == b
        False
        """
        return (
            self._top_row == other._top_row and
            self._middle_row == other._middle_row and
            self._bottom_row == other._bottom_row
        )

    def place_token(self, x, y, token):
        """Place a token character string at a given coordinate.

        (top-left is 0, 0), x is horizontal position, y is vertical position

        >>> a = Board()
        >>> a._top_row = ['', 'X', 'O']
        >>> a.place_token(0, 0, 'O')
        >>> a
        Board(['O', 'X', 'O'], ['', '', ''], ['', '', ''])
        >>> a = Board()
        >>> a._top_row = ['', 'X', 'O']
        >>> a.place_token(0, 1, 'O')
        >>> a
        Board(['', 'X', 'O'], ['O', '', ''], ['', '', ''])
        """
        y_to_row = {0: self._top_row, 1: self._middle_row, 2:self._bottom_row}
        (y_to_row[y])[x] = token

    def calc_winner(self):
        """Determines what token string has won or returns None if no one has

        >>> a = Board()
        >>> a._top_row = ['', '', '']
        >>> a._middle_row = ['', '', '']
        >>> a._bottom_row = ['', '', '']
        >>> a.calc_winner()
        None

        >>> a = Board()
        >>> a._top_row = ['X', 'X', 'O']
        >>> a._middle_row = ['O', 'O', 'X']
        >>> a._bottom_row = ['X', 'O', 'X']
        >>> a.calc_winner()
        None

        >>> a = Board()
        >>> a._top_row = ['', '', '']
        >>> a._middle_row = ['', '', '']
        >>> a._bottom_row = ['X', 'X', 'X']
        >>> a.calc_winner()
        'X'

        >>> a = Board()
        >>> a._top_row = ['', '', 'O']
        >>> a._middle_row = ['', '', 'O']
        >>> a._bottom_row = ['', '', 'O']
        >>> a.calc_winner()
        'O'

        >>> a = Board()
        >>> a._top_row = ['X', '', 'O']
        >>> a._middle_row = ['', 'X', '']
        >>> a._bottom_row = ['', '', 'X']
        >>> a.calc_winner()
        'X'
        """
        if (
                self._middle_row[0] == self._middle_row[1] == self._middle_row[2] or
                self._top_row[1] == self._middle_row[1] == self._bottom_row[1] or
                self._top_row[0] == self._middle_row[1] == self._bottom_row[2] or
                self._top_row[2] == self._middle_row[1] == self._bottom_row[0]
        ):
            return self._middle_row[1]
        elif (
                self._top_row[0] == self._top_row[1] == self._top_row[2] or
                self._top_row[0] == self._middle_row[0] == self._bottom_row[0]
        ):
            return self._top_row[0]
        elif (
                self._bottom_row[0] == self._bottom_row[1] == self._bottom_row[2] or
                self._top_row[2] == self._middle_row[2] == self._bottom_row[2]
        ):
            return self._bottom_row[2]
        else:
            return None