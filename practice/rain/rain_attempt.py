""" Opens a Rain Text File and Mines for information. I'm using "cells" for rows, and "boxes" for columns"""

from collections import namedtuple

TEST_ROWS = [['23', 'MAR', '2016', '12'], ['22', 'MAR', '2016', '1'], ['21', 'MAR', '2016', '8']]
TEST_COLUMNS = [['23', '22', '21'], ['MAR', 'MAR', 'MAR'], ['2016', '2016', '2016'], ['12', '1', '8']]


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


def cast_rainfall_to_int(row):
    """ Takes in a row of data and converts the rainfall value to an intiger"""


def split_single_line_to_single_row(text):
    """Splits a row of text by triple spaces into a list of strings. It then splits the first item in the list of
    strings from kebab-case to another list of strings.

    >>> split_single_line_to_single_row('four-five-six   one   two   three' )
    ['four-five-six', 'one']
    """
    simple_row = text.split('   ')

    final_row = simple_row[:2]
    return final_row


def split_lines_to_rows(text):
    """Splits all lines of text into several rows in the form of lists of strings.

    >>> split_lines_to_rows(['Charmander   Bulbasuar   Squirtle','Ponya   Oddish   Magicarp','Fire   Plant   Water'])
    [['Charmander', 'Bulbasuar'], ['Ponya', 'Oddish'], ['Fire', 'Plant]]
    """
    rows = [split_single_line_to_single_row(line) for line in text]
    return rows


# def convert_rows_to_columns(rows):
#     """Takes rows as lists of strings, and transforms them into columns as lists of strings
#
#     >>> convert_rows_to_columns([['Char', 'Bulb', 'Squirt'],['Ponya', 'Oddish', 'Magicarp'],['Fire', 'Plant', 'Water']])
#     [['Char', 'Ponya', 'Fire'], ['Bulb', 'Oddish', 'Plant'], ['Squirt', 'Magicarp', 'Water']]
#     """
#     columns_by_tuple = list(zip(*rows))
#     columns = [list(tup) for tup in columns_by_tuple]
#     return columns


def convert_row_of_data_to_named_tuple(row_of_data):
    """Takes in a single row of data and converts it into a named tuple

    >>> convert_row_of_data_to_named_tuple(['MAR-5-2016', '17'])

    """
    namedtuple('DateAndRainfall', ['date', 'rainfall'])
    return DateAndRainfall(row_of_data[0], row_of_data[1])


def convert_rows_of_data_to_named_tuples(rows_of_data):
    """Takes in a list of lists, and converts the internal lists to named tuples

    >>> convert_rows_of_data_to_named_tuples(['MAR-5-2016', '17'],['MAR-6-2016', '19'])

    """
    return [convert_row_of_data_to_named_tuple(row) for row in rows_of_data]


def get_most_daily_rain_inches(rows_of_data):
    """Gets the value of the most rain for any given date

    # >>> get_most_daily_rain_inches([['1', '2', '3', '8'], ['4', '5', '6', '1'], ['7', '8', '9', '12'], \
    # ['4', '7', '6', '1']])
    # '0.07'
    """
    dates_and_rainfalls = connvert_rows_of_data_to_named_tuples(rows_of_data)
    max(dates_and_rainfalls)

    # return max rainfall from dates_and_rainfalls


    return most_rain_inches


def get_index_of_max_daily_rain_box(columns):
    """Takes in rows of data, and returns index of day with most rain columns max rain

    >>> get_index_of_max_daily_rain_box(TEST_COLUMNS)
    0
    """
    rainy_days = [int(value) for value in columns[3] if value.isdigit()]
    daily_rain_values = [value for value in rainy_days]
    day_index_of_max_daily_rain = daily_rain_values.index(max(daily_rain_values))
    return day_index_of_max_daily_rain


def get_day_with_most_rain(rows, columns):
    """Returns the date of day with the most rain

    >>> get_day_with_most_rain(TEST_ROWS, TEST_COLUMNS)
    'MAR 23 2016'
    """
    index_of_day_cell = get_index_of_max_daily_rain_box(columns)
    day_full_line = rows[index_of_day_cell]
    date = day_full_line[1] + ' ' + day_full_line[0] + ' ' + day_full_line[2]
    return date


def output_for_max_rain_date(most_rain, date_with_most_rain):
    """Prints the day with the most rain, and how much rain fell in inches.

    >>> output_for_max_rain_date('5','30-MAR-2016')
    The day with the most rain was 30-MAR-2016, which had 5 inches of rain!
    """
    print('The day with the most rain was {}, which had {} inches of rain!'.format(date_with_most_rain, most_rain))


def get_year(row):
    """Calculates Grouping Key.

    >>> get_year(['23', 'Mar', '2016'])
    '2016'
    """
    return row[2]


# def get_year_to_rows(rows):
#     """Creates a dictionary of rows of data keyed to each year.
#
#     >>> get_year_to_rows([['23', 'Mar', '2016'], ['21', 'Feb', '2016']])
#     {'2016': [['23', 'Mar', '2016'], ['21', 'Feb', '2016']]}
#     """
#
#     year_to_rows = {
#         group_key: list(grouped_rows)
#         for group_key, grouped_rows
#         in groupby(rows, get_year)
#         }
#     return year_to_rows


def get_years_to_annual_rain(rows):
    """Transforms a dictionary of years to data to years to total rain.

    >>> get_years_to_annual_rain([['30', 'MAR', '2016', '7'], ['29', 'MAR', '2017', '9']])
    [['2016'] [[3]]], [['2017'] [[7]]]
    """
    year_to_rows = get_year_to_rows(rows)
    years_to_annual_rain = {}
    for year in year_to_rows:
        print(year_to_rows[year])
        annual_data = year_to_rows[year]
        annual_rain_values = [(value[3]) for value in annual_data]
        total_annual_rain = sum(annual_rain_values)
        year_to_annual_rain = {year: total_annual_rain}
        years_to_annual_rain.update(year_to_annual_rain)
    return years_to_annual_rain


def group_by(iterable, key):
    """Place each item in an iterable into a bucket based on calling the key
    function on the item."""
    group_to_items = {}
    for item in iterable:
        group = key(item)
        if group not in group_to_items:
            group_to_items[group] = []
        group_to_items[group].append(item)
    return group_to_items


def get_years_to_daily_rain(rows_of_data):
    """Groups rows of data into dictionaries of daily rain keyed off of year.

    >>> get_year_with_most_rain(TEST_ROWS)
    '2016'
    """

    years =
    years_to_daily_rain = group_by(rows_of_data, key)


def get_year_with_most_rain(rows_of_data):
    """Runs rows of data through functions to output year with most rainfall.

    >>> get_year_with_most_rain(TEST_ROWS)
    '2016'
    """
    years_to_daily_rain = get_years_to_daily_rain(rows_of_data)

    years_to_annual_rain = get_years_to_annual_rain(rows_of_data)

    # year_with_most_rain = max(years_to_annual_rain.keys(), key=(lambda k: years_to_annual_rain[k]))
    # # found on Stack Overflow: http://tinyurl.com/jdjs5p6
    return year_with_most_rain


def output_for_year(year):
    """Prints the year with the most rain.

    >>> output_for_year('2015')
    The year with the most rain was 2015!
    """
    print('The year with the most rain was {}!'.format(year))


def main():
    """Main function."""
    text_lines = open_file('rain.txt')
    table_as_text_lines = cut_non_data(text_lines)
    rows_of_data = split_lines_to_rows(table_as_text_lines)
    # columns_of_data = convert_rows_to_columns(rows_of_data)

    most_inches_of_rain_in_single_date = get_most_daily_rain_inches(rows_of_data)
    date_with_most_rain = get_day_with_most_rain(rows_of_data, columns_of_data)

    year_with_most_rain = get_year_with_most_rain(rows_of_data)

    output_for_max_rain_date(most_inches_of_rain_in_single_date, date_with_most_rain)
    output_for_year(year_with_most_rain)


if __name__ == '__main__':
    main()
