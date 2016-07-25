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


def cut_non_valid_data(rows_of_data):
    """Takes in a list of rows of data, and returns that list omitting entries that lack a numeral in second token

    >>> cut_non_valid_data([['Date1', '1'], ['Date2', '2'], ['Date3', '-']])
    [['Date1', '1'], ['Date2', '2']]
    """
    return [row for row in rows_of_data if row[1].isdigit()]

def convert_row_to_dictionary(row):
    """Converts an array into a dictionary

    >>> convert_row_to_dictionary(['Date1', '1'])
    {'date': 'Date1', 'rainfall': '1'}
    """
    date_to_rainfall = {}
    date_to_rainfall['date'] = row[0]
    date_to_rainfall['rainfall'] = row[1]
    return date_to_rainfall

def convert_rows_to_dictionaries(rows_of_data):
    """Converts the list of arrays into a list of dictionaries

       >>> convert_rows_to_dictionaries([['Date1', '1'], ['Date2', '2']])
       [{'date': 'Date1', 'rainfall': '1'}, {'date': 'Date2', 'rainfall': '2'}]
       """
    return [convert_row_to_dictionary(row) for row in rows_of_data]


def get_key(dictionary):
    """

    >>> get_key({'date': '12-JAN-2016', 'rainfall': '105'})
    '105'
    """
    return dictionary['rainfall']


def get_day_with_most_rain(dates_to_dates_and_rainfall_to_value):
    """

    >>> get_day_with_most_rain([{'date': '12-JAN-2016', 'rainfall': '105'}, {'date': '13-JAN-2016', 'rainfall': '106'}])
    {'date': '13-JAN-2016', 'rainfall': '106'}
    """
    dictionary = max(dates_to_dates_and_rainfall_to_value, key=get_key)
    return dictionary


def main():
    """Main function."""
    text_lines = open_file('rain.txt')
    table_as_text_lines = cut_non_data(text_lines)
    rows_of_data = split_lines_to_rows_of_relevant_data(table_as_text_lines)
    rows_of_complete_data = cut_non_valid_data(rows_of_data)
    dates_to_dates_and_rainfall_to_value = convert_rows_to_dictionaries(rows_of_complete_data)
    day_with_most_rain = get_day_with_most_rain(dates_to_dates_and_rainfall_to_value)


    print(dictionaries_of_data)


if __name__ == '__main__':
    main()
