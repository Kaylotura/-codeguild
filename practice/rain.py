""" Opens a Rain Text File and Mines for information. I'm using "cells" for rows, and "boxes" for columns"""


def open_file():
    """Opens text file for analysis."""
    with open('rain.txt', 'r') as table_file:
        lines_of_text = table_file.readlines()
    return lines_of_text


def cut_non_data(text):
    """Cuts lines of text after table line

    >>> ['Apple Pie', 'Hamburgers'
    >>> '------------------------------------------------------------------------------------------------------------------\n',
    >>> 'lovely']
    ['lovely']
    """
    TABLE_LINE_CUT_OFF = '------------------------------------------------------------------------------------------------------------------\n'
    table_start_index = text.index(TABLE_LINE_CUT_OFF) + 1
    table_as_text_lines = text[table_start_index:]
    return table_as_text_lines


def split_single_line_to_single_row(text):
    """Splits a single line of text into a row in the form of a list of strings.

    >>> ['one    two    three' ]
    ['one','two','three']
    """
    simple_row = text.split('   ')
    full_date = simple_row[0]
    split_dates = full_date.split('-')
    final_row = split_dates + simple_row[1:]
    print(final_row)
    return final_row


def split_lines_to_rows(text):
    """Splits all lines of text into several rows in the form of lists of strings
    >>> split_lines_to_rows([['Charmander Bulbasuar Squirtle'],['Ponya Oddish Magicarp'],['Fire Plant Water']])
    [['Charmander', 'Bulbasuar', 'Squirtle'],['Ponya', 'Oddish', 'Magicarp'],['Fire', 'Plant', 'Water']]
    """
    # dates_as_lists = get_dates_as_lists(text)
    rows = [split_single_line_to_single_row(line) for line in text]
    return rows


def convert_rows_to_columns(rows):
    """Takes rows as lists of strings, and transforms them into columns as lists of strings
    >>> [['Charmander', 'Bulbasuar', 'Squirtle'],['Ponya', 'Oddish', 'Magicarp'],['Fire', 'Plant', 'Water']]
    [['Charmander', 'Ponya'', 'Fire'],['Bulbasuar', 'Oddish', 'Plant'],['Squirtle', 'Magicarp', 'Water']]
    """
    columns_by_tuple = list(zip(*rows))
    columns = [list(tup) for tup in columns_by_tuple]
    return columns


def get_most_daily_rain_inches(columns):
    """Gets the value of the most rain for any given date

    >>> get_most_daily_rain_inches([['1', '2', '3', '8'], ['4', '5', '6', '1'], ['7', '8', '9', '12'], \
    ['4', '7', '6', '1']])
    '0.07'
    """
    most_rain = max(columns[3])
    most_rain_inches = str(int(most_rain) / 100)
    return most_rain_inches


def get_index_of_max_daily_rain_box(columns):
    """Takes in rows of data, and returns index of day with most rain columns max rain

    >>> get_day_with_most_rain([['1', '2', '3', '8'], ['4', '5', '6', '1'], ['7', '8', '9', '12'],
    >>> ['4', '7', '6', '1']])
    '2'
    """
    day_index_of_max_daily_rain = columns[3].index(max(columns[3]))
    return day_index_of_max_daily_rain


def get_day_with_most_rain(rows, columns):
    index_of_day_cell = get_index_of_max_daily_rain_box(columns)
    day_full_line = rows[index_of_day_cell]
    date = day_full_line[1] + ' ' + day_full_line[0] + ' ' + day_full_line[2]
    return date


def output_for_max_rain_date(most_rain, date_with_most_rain):
    print('The day with the most rain was ' + date_with_most_rain + ', which had ' + most_rain + ' inches of rain.')


# def get_most_anual_rain_inches():


def main():
    text_lines = open_file()
    table_as_text_lines = cut_non_data(text_lines)

    rows_of_data = split_lines_to_rows(table_as_text_lines)
    columns_of_data = convert_rows_to_columns(rows_of_data)
    most_inches_of_rain_in_single_date = get_most_daily_rain_inches(columns_of_data)
    date_with_most_rain = get_day_with_most_rain(rows_of_data, columns_of_data)
    # most_inches_of_rain_in_a_year = get_most_anual_rain_inches(...)
    # year_with_most_rain = get_year_with_most_rain(...)
    output_for_max_rain_date(most_inches_of_rain_in_single_date, date_with_most_rain)
    # output_for_max_rain_date(...)

if __name__ == '__main__':
    main()