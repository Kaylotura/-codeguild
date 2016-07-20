""" Opens a Rain Text File and Mines for information. I'm using "cells" for rows, and "boxes" for columns"""


from itertools import groupby


TEST_ROWS = [['23', 'MAR', '2016', '12'], ['22', 'MAR', '2016', '1'], ['21', 'MAR', '2016', '8']]
TEST_COLUMNS = [['23', '22', '21'], ['MAR', 'MAR', 'MAR'], ['2016', '2016', '2016'], ['12', '1', '8']]


def open_file(file):
    """Opens text file for analysis.

    >>> open_file('rain_text/testrain.txt')
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


def split_single_line_to_single_row(text):
    """Splits a single line of text into a row in the form of a list of strings.

    >>> split_single_line_to_single_row('one   two   three' )
    ['one', 'two', 'three']
    >>> split_single_line_to_single_row('one-two-three')
    ['one', 'two', 'three']
    """
    simple_row = text.split('   ')
    full_date = simple_row[0]
    split_dates = full_date.split('-')
    final_row = split_dates + simple_row[1:]
    return final_row


def split_lines_to_rows(text):
    """Splits all lines of text into several rows in the form of lists of strings.

    >>> split_lines_to_rows(['Charmander Bulbasuar Squirtle','Ponya Oddish Magicarp','Fire Plant Water'])
    [['Charmander Bulbasuar Squirtle'], ['Ponya Oddish Magicarp'], ['Fire Plant Water']]
    """
    rows = [split_single_line_to_single_row(line) for line in text]
    return rows


def convert_rows_to_columns(rows):
    """Takes rows as lists of strings, and transforms them into columns as lists of strings

    >>> convert_rows_to_columns([['Char', 'Bulb', 'Squirt'],['Ponya', 'Oddish', 'Magicarp'],['Fire', 'Plant', 'Water']])
    [['Char', 'Ponya', 'Fire'], ['Bulb', 'Oddish', 'Plant'], ['Squirt', 'Magicarp', 'Water']]
    """
    columns_by_tuple = list(zip(*rows))
    columns = [list(tup) for tup in columns_by_tuple]
    return columns


def contains_numeral(value):
    """Filtering function, returns boolean if string is numeric.
    >>> contains_numeral('13')
    True
    >>> contains_numeral('pie')
    False
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def get_most_daily_rain_inches(columns):
    """Gets the value of the most rain for any given date

    >>> get_most_daily_rain_inches([['1', '2', '3', '8'], ['4', '5', '6', '1'], ['7', '8', '9', '12'], \
    ['4', '7', '6', '1']])
    '0.07'
    """
    rainy_days = [int(value) for value in columns[3] if contains_numeral(value)]
    most_rain = max(rainy_days)
    most_rain_inches = str(int(most_rain) / 100)
    return most_rain_inches


def get_index_of_max_daily_rain_box(columns):
    """Takes in rows of data, and returns index of day with most rain columns max rain

    >>> get_index_of_max_daily_rain_box(TEST_COLUMNS)
    0
    """
    rainy_days = [int(value) for value in columns[3] if contains_numeral(value)]
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


def get_year_to_rows(rows):
    """Creates a dictionary of rows of data keyed to each year.

    >>> get_year_to_rows([['23', 'Mar', '2016'], ['21', 'Feb', '2016']])
    {'2016': [['23', 'Mar', '2016'], ['21', 'Feb', '2016']]}
    """
    year_to_rows = {
        group_key: list(grouped_rows)
        for group_key, grouped_rows
        in groupby(rows, get_year)
        }
    return year_to_rows


def sum_yearly_rainfall(year, year_to_daily_rain):
    """Returns sum of yearly rainfall as an integer value

    >>> sum_yearly_rainfall('2016', {['2016': [['1'], ['2']]]})
    3
    """
    rain_fall_values = year_to_daily_rain[year]
    daily_rain_values = [int(value) for value in rain_fall_values[3] if contains_numeral(value)]
    total = sum(daily_rain_values)
    return total


def get_years_to_annual_rain(rows):
    """Transforms a dictionary of years to data to years to total rain.

    >>> get_years_to_annual_rain({[['2016']: [['1'], ['2']]], [['2017']: [['3'], ['4']]]})
    {[['2016']: [[3]]], [['2017']: [[7]]]
    """
    year_to_rows = get_year_to_rows(rows)
    years_to_annual_rain = {}
    for year in year_to_rows:
        annual_data = year_to_rows[year]
        annual_rain_values = [int(value) for value in annual_data[3] if contains_numeral(value)]
        total_annual_rain = sum(annual_rain_values)
        year_to_annual_rain = {year: total_annual_rain}
        years_to_annual_rain.update(year_to_annual_rain)
    return years_to_annual_rain


def get_year_with_most_rain(rows):
    """Runs rows of data through functions to output year with most rainfall.

    >>> get_year_with_most_rain(TEST_ROWS)
    '2016'
    """
    years_to_annual_rain = get_years_to_annual_rain(rows)
    year_with_most_rain = max(years_to_annual_rain.keys(), key=(lambda k: years_to_annual_rain[k]))
    # found on Stack Overflow: http://tinyurl.com/jdjs5p6
    return year_with_most_rain


def output_for_year(year):
    """ Prints the year with the most rain.

    >>> output_for_year('2015')
    The year with the most rain was 2015!
    """
    print('The year with the most rain was {}!'.format(year))


def main():
    """Main function."""
    text_lines = open_file('rain_text/rain.txt')
    table_as_text_lines = cut_non_data(text_lines)
    rows_of_data = split_lines_to_rows(table_as_text_lines)
    columns_of_data = convert_rows_to_columns(rows_of_data)
    most_inches_of_rain_in_single_date = get_most_daily_rain_inches(columns_of_data)
    date_with_most_rain = get_day_with_most_rain(rows_of_data, columns_of_data)
    year_with_most_rain = get_year_with_most_rain(rows_of_data)
    output_for_max_rain_date(most_inches_of_rain_in_single_date, date_with_most_rain)
    output_for_year(year_with_most_rain)

if __name__ == '__main__':
    main()
