"""" Opens a Rain Text File and Mines for information"""

def open_file():
    """Opens text file for analysis"""
    with open('rainspoof.txt', 'r') as table_file:
        lines_of_text = table_file.readlines()
    return lines_of_text


def split_single_line_to_single_row(text):
    """Splits a single line of text into a row in the form of a list of strings"""
    return text.split(' ')

def split_lines_to_rows(text):
    """Splits all lines of text into several rows in the form of lists of strings
    >>> split_lines_to_rows([['Charmander Bulbasuar Squirtle'],['Ponya Oddish Magicarp'],['Fire Plant Water']])
    [['Charmander', 'Bulbasuar', 'Squirtle'],['Ponya', 'Oddish', 'Magicarp'],['Fire', 'Plant', 'Water']]
      """
    rows = [split_lines_to_rows(line) for line in text]
    return rows

def convert_row_to_column(row):
    """Takes a single row as lists of strings, and transforms it into a column as lists of strings"""
    column = list(zip(*row))

def convert_rows_to_columns(rows):
    """Takes rows as lists of strings, and transforms them into columns as lists of strings
    >>> [['Charmander', 'Bulbasuar', 'Squirtle'],['Ponya', 'Oddish', 'Magicarp'],['Fire', 'Plant', 'Water']]
    [['Charmander', 'Ponya'', 'Fire'],['Bulbasuar', 'Oddish', 'Plant'],['Squirtle', 'Magicarp', 'Water']]
    """
    columns = [convert_row_to_column(row) for row in rows]


def main():
    lines_of_text = open_file()
    rows_of_data = split_lines_to_rows(lines_of_text)
    columns_of_data = convert_rows_to_columns(rows_of_data)

if __name__ == '__main__':
    main()

