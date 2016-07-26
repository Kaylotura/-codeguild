"""Class Module for Tic-Tac-Toe game that handles the board as a row-first list of lists."""


class ListTTTBoard:
    """Creates a Board class to operate within."""
    def __init__(self):
        """Initialize Class
        >>> a = ListTTTBoard()
        >>> a
        ListTTTBoard([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
        """
        self._rows = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def __repr__(self):
        """Return representation.

        >>> a = ListTTTBoard()
        >>> a._rows = [[' ', 'X', 'O'], [' ', ' ', ' '], [' ', ' ', ' ']]
        >>> a
        ListTTTBoard([[' ', 'X', 'O'], [' ', ' ', ' '], [' ', ' ', ' ']])
        """
        return 'ListTTTBoard({!r})'.format(self._rows)

    def __eq__(self, other):
        """Defines equality.

        >>> a = ListTTTBoard()
        >>> a._rows = [[' ', 'X', 'O'], [' ', ' ', ' '], [' ', ' ', ' ']]
        >>> b = ListTTTBoard()
        >>> b._rows = [[' ', 'X', 'O'], [' ', ' ', ' '], [' ', ' ', ' ']]
        >>> a == b
        True
        >>> a = ListTTTBoard()
        >>> a._rows = [[' ', 'X', 'O'], [' ', ' ', ' '], [' ', ' ', ' ']]
        >>> b = ListTTTBoard()
        >>> b._rows = [[' ', 'X', 'O'], [' ', 'O', 'X'], [' ', ' ', ' ']]
        >>> a == b
        False
        """
        return (
            self._rows == other._rows
        )

    def place_token(self, x, y, token):
        """Place a token character string at a given coordinate.

        (top-left is 0, 0), x is horizontal position, y is vertical position

        >>> a = ListTTTBoard()
        >>> a._rows = [[' ', 'X', 'O'], [' ', ' ', ' '], [' ', ' ', ' ']]
        >>> a.place_token(0, 0, 'O')
        >>> a
        ListTTTBoard([['O', 'X', 'O'], [' ', ' ', ' '], [' ', ' ', ' ']])
        >>> a = ListTTTBoard()
        >>> a._rows = [[' ', 'X', 'O'], [' ', ' ', ' '], [' ', ' ', ' ']]
        >>> a.place_token(0, 1, 'O')
        >>> a
        ListTTTBoard([[' ', 'X', 'O'], ['O', ' ', ' '], [' ', ' ', ' ']])
        """
        (self._rows[y])[x] = token

    def calc_winner(self):
        """Determines what token string has won or returns None if no one has

        >>> a = ListTTTBoard()
        >>> a._rows = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        >>> a.calc_winner() == None
        True

        >>> a = ListTTTBoard()
        >>> a._rows = [
        ... ['X', 'X', 'O'],
        ... ['O', 'O', 'X'],
        ... ['X', 'O', 'X']
        ... ]
        >>> a.calc_winner() != None
        False

        >>> a = ListTTTBoard()
        >>> a._rows = [
        ... [' ', ' ', ' '],
        ... [' ', ' ', ' '],
        ... ['X', 'X', 'X']
        ... ]
        >>> a.calc_winner()
        'X'

        >>> a = ListTTTBoard()
        >>> a._rows = [
        ... [' ', ' ', 'O'],
        ... [' ', ' ', 'O'],
        ... ['X', 'X', 'O']
        ... ]
        >>> a.calc_winner()
        'O'

        >>> a = ListTTTBoard()
        >>> a._rows = [
        ... ['X', ' ', ' '],
        ... ['O', 'X', 'O'],
        ... ['O', 'X', 'X']
        ... ]
        >>> a.calc_winner()
        'X'
        """
        win_lines = [
            [(self._rows[1])[0], (self._rows[1])[1], (self._rows[1])[2]],
            [(self._rows[0])[1], (self._rows[1])[1], (self._rows[2])[1]],
            [(self._rows[0])[0], (self._rows[1])[1], (self._rows[2])[2]],
            [(self._rows[0])[2], (self._rows[1])[1], (self._rows[2])[0]],
            [(self._rows[0])[0], (self._rows[0])[1], (self._rows[0])[2]],
            [(self._rows[0])[0], (self._rows[1])[0], (self._rows[2])[0]],
            [(self._rows[2])[0], (self._rows[2])[1], (self._rows[2])[2]],
            [(self._rows[0])[2], (self._rows[1])[2], (self._rows[0])[2]]
        ]
        if ['X','X','X'] in WIN_LINES:
            return 'X'
        elif ['O','O','O'] in WIN_LINES:
            return 'O'
        else:
            return None

    def __str__(self):
        r"""Returns a pretty-printed picture of the board.

        >>> a = ListTTTBoard()
        >>> a._rows = [
        ... ['X', 'X', 'O'],
        ... ['O', 'O', 'X'],
        ... ['X', ' ', 'X']
        ... ]
        >>> a.__str__()
        'X|X|O\nO|O|X\nX| |X'
        """
        return self._rows[0][0] + '|' + self._rows[0][1] + '|' + self._rows[0][2] + '\n' +\
               self._rows[1][0] + '|' + self._rows[1][1] + '|' + self._rows[1][2] + '\n' +\
               self._rows[2][0] + '|' + self._rows[2][1] + '|' + self._rows[2][2]
