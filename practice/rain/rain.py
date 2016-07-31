""" Opens a Rain Text File and returns information regarding day with most rain and year with most rain."""


from collections import namedtuple


DayEntry = namedtuple('DayEntry', ['date', 'rainfall'])
YearEntry = namedtuple('YearEntry', ['year', 'rainfall'])


def open_file(data_file):
    """Opens text file for analysis.

    >>> open_file('testrain.txt')
    ['She took all my money    And my best friend    You know the story    Here it comes again']
    """
    with open(data_file, 'r') as table_file:
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

    >>> split_single_line_to_relevant_data('four-five-six   1   2   3' )
    ['four-five-six', 1]
    """
    simple_row = line.split('   ')
    final_row = simple_row[:2]
    if final_row[1].isdigit():
        final_row[1] = int(final_row[1])
    return final_row


def split_lines_to_rows_of_relevant_data(lines):
    """Splits all lines of text into several rows in the form of lists of strings.

    >>> split_lines_to_rows_of_relevant_data(['Charmander   1   3',
    ... 'Ponya   2   4','Fire   3   6'])
    [['Charmander', 1], ['Ponya', 2], ['Fire', 3]]
    """
    rows = [split_single_line_to_relevant_data(line) for line in lines]
    return rows


def cut_non_valid_data(rows_of_data):
    """Takes in a list of rows of data, and returns that list omitting entries that lack a numeral in second token

    >>> cut_non_valid_data([['Date1', '1'], ['Date2', '2'], ['Date3', '-']])
    [['Date1', '1'], ['Date2', '2']]
    """
    return [row for row in rows_of_data if type(row[1]) == int]


def convert_row_to_day_entry(row):
    """Converts a row into a DayEntry named tuple

    >>> convert_row_to_day_entry(['13-JAN-2016', 107])
    DayEntry(date='13-JAN-2016', rainfall=107)
    """
    return DayEntry(row[0], row[1])


def convert_rows_to_day_entries(rows_of_data):
    """Converts a row of lists into a list of Day Entry tuples

    >>> convert_rows_to_day_entries([['13-JAN-2016', 107],['15-SEP-2002', 75]])
    [DayEntry(date='13-JAN-2016', rainfall=107), DayEntry(date='15-SEP-2002', rainfall=75)]

    """
    return [convert_row_to_day_entry(row) for row in rows_of_data]


def get_daily_rainfall_key(day_entry):
    """Gets rainfall amount key for comparing.

    >>> get_daily_rainfall_key(DayEntry(date='13-JAN-2016', rainfall=107))
    107
    """
    return day_entry.rainfall


def get_day_with_most_rain(day_entries):
    """

    >>> get_day_with_most_rain([DayEntry(date='13-JAN-2016', rainfall=107),
    ... DayEntry(date='15-SEP-2002', rainfall=75)])
    DayEntry(date='13-JAN-2016', rainfall=107)
    """
    return max(day_entries, key=get_daily_rainfall_key)


def output_day_with_most_rain(day_entry):
    """Prints a string informing of the date of the most rain, with the total rainfall in inches

    >>> output_day_with_most_rain(DayEntry(date='13-JAN-2016', rainfall=107))
    13-JAN-2016 had the most rain with 1.07 inches of rain.
    """
    rain_inches = str(day_entry.rainfall / 100)
    date = day_entry.date
    print('{} had the most rain with {} inches of rain.'.format(date, rain_inches))


def get_year_key(day_entry):
    """Gets key of Year from day entry

    >>> get_year_key(DayEntry(date='13-JAN-2016', rainfall=107))
    '2016'
    """
    return day_entry.date[-4:]


def group_by_year(day_entries):
    """Place each item in an iterable into a bucket based on calling the key function on the item.

    >>> group_by_year(([DayEntry(date='13-JAN-2016', rainfall=107),
    ... DayEntry(date='15-SEP-2002', rainfall=75)])) ==  {'2016': [DayEntry(date='13-JAN-2016', rainfall=107)],
    ... '2002': [DayEntry(date='15-SEP-2002', rainfall=75)]}
    True
    """
    group_to_items = {}
    for item in day_entries:
        group = get_year_key(item)
        if group not in group_to_items:
            group_to_items[group] = []
        group_to_items[group].append(item)
    return group_to_items


def convert_from_year_to_day_entry_to_year_entry(year_to_day_entry):
    """Takes in a tuple of a given year and a DayEntry, and converts it to a YearEntry.

    >>> convert_from_year_to_day_entry_to_year_entry(
    ... ('2016', [DayEntry(date='13-JAN-2016', rainfall=107), DayEntry(date='15-JAN-2016', rainfall=13)]))
    YearEntry(year='2016', rainfall=120)
    """
    year = year_to_day_entry[0]
    day_entries = year_to_day_entry[1]
    rainfalls = [item.rainfall for item in day_entries]
    rainfall = sum(rainfalls)
    return YearEntry(year, rainfall)


def convert_from_year_to_day_entries_to_year_entries(year_to_day_entries):
    """Converts year to day entries dictionaries to a YearlyEntry named tuple for year and total rainfall.

    >>> a = convert_from_year_to_day_entries_to_year_entries(
    ... {'2016': [DayEntry(date='13-JAN-2016', rainfall=107), DayEntry(date='15-SEP-2016', rainfall=3)],
    ... '2002': [DayEntry(date='15-SEP-2002', rainfall=75), DayEntry(date='16-JUN-2002', rainfall=25)]}
    ... )
    >>> sorted(a)
    [YearEntry(year='2002', rainfall=100), YearEntry(year='2016', rainfall=110)]
    """
    return [convert_from_year_to_day_entry_to_year_entry(year) for year in list(year_to_day_entries.items())]


def get_yearly_rainfall_key(year_entry):
    """Gets rainfall amount key for comparing.

    >>> get_yearly_rainfall_key(YearEntry(year='2016', rainfall=100))
    100
    """
    return year_entry.rainfall


def get_year_with_most_rain(year_entries):
    """Takes in a list of YearEntries and returns the YearEntry with the most rain.

    >>> get_year_with_most_rain([YearEntry(year='2016', rainfall=100),
    ... YearEntry(year='2012', rainfall=80)])
    YearEntry(year='2016', rainfall=100)
    """
    return max(year_entries, key=get_daily_rainfall_key)


def output_year_with_most_rain(year_entry):
    """Prints a string informing of the year of the most rain, with the total rainfall in inches

    >>> output_year_with_most_rain(YearEntry(year='2016', rainfall=150))
    2016 had the most rain with 1.5 inches of rain.
    """
    rain_inches = str(year_entry.rainfall / 100)
    year = year_entry.year
    print('{} had the most rain with {} inches of rain.'.format(year, rain_inches))


def main():
    """Main function."""
    text_lines = open_file('rain.txt')
    table_as_text_lines = cut_non_data(text_lines)
    rows_of_data = split_lines_to_rows_of_relevant_data(table_as_text_lines)
    rows_of_complete_data = cut_non_valid_data(rows_of_data)
    day_entries = convert_rows_to_day_entries(rows_of_complete_data)
    day_with_most_rain = get_day_with_most_rain(day_entries)
    output_day_with_most_rain(day_with_most_rain)
    year_to_day_entries = group_by_year(day_entries)
    yearly_entries = convert_from_year_to_day_entries_to_year_entries(year_to_day_entries)
    year_with_most_rain = get_year_with_most_rain(yearly_entries)
    output_year_with_most_rain(year_with_most_rain)

if __name__ == '__main__':
    main()
