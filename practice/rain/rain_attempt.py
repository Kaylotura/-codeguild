""" Opens a Rain Text File and returns information regarding day with most rain and year with most rain."""


def open_file(file):
    """Opens text file for analysis.

    >>> open_file('testrain.txt')
    ['She took all my money    And my best friend    You know the story    Here it comes again']
    """
    with open(file, 'r') as table_file:
        lines_of_text = table_file.readlines()
    return lines_of_text


def cut_non_data(text):
    """Cuts lines of text after table line.

    >>> cut_non_data([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14]])
    [[12], [13], [14]]
    """
    table_as_text_lines = text[11:]
    return table_as_text_lines


def split_single_line_to_relevant_data(line):
    """Splits a row of text by triple spaces into a list of strings, and saves the first two items.

    >>> split_single_line_to_relevant_data('four-five-six   one   two   three' )
    ['four-five-six', 'one']
    """
    simple_row = line.split('   ')
    final_row = simple_row[:2]
    return final_row


def split_lines_to_rows_of_relevant_data(lines):
    """Splits all lines of text into several rows in the form of lists of strings.

    >>> split_lines_to_rows_of_relevant_data(['Charmander   Bulbasuar   Squirtle','Ponya   Oddish   Magicarp','Fire   Plant   Water'])
    [['Charmander', 'Bulbasuar'], ['Ponya', 'Oddish'], ['Fire', 'Plant']]
    """
    rows = [split_single_line_to_relevant_data(line) for line in lines]
    return rows


def cut_non_numerals_and_cast_rainfall_as_int(rows_of_data):
    """Takes in a list of rows of data, and returns that list omitting entries that lack a numeral in second token

    >>> cut_non_numerals_and_cast_rainfall_as_int(['Date1', '1'], ['Date2', '2'], ['Date3', '-'])
    [['Date1', 1], ['Date2', 2]]
    """

def main():
    """Main function."""
    text_lines = open_file('rain.txt')
    table_as_text_lines = cut_non_data(text_lines)
    rows_of_data = split_lines_to_rows_of_relevant_data(table_as_text_lines)
    rows_of_complete_data = cut_non_numerals_and_cast_rainfall_as_int(rows_of_data)


if __name__ == '__main__':
    main()


