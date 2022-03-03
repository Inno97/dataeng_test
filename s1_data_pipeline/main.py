"""
This module processes two datasets in CSV, on a regular interval (e.g. daily).

Processing tasks:
    - Split the `name` field into `first_name`, and `last_name`
    - Remove any zeros prepended to the `price` field
    - Delete any rows which do not have a `name`
    - Create a new field named `above_100`, which is `true` if the price is strictly greater than 
      100

It can be run as a cronjob.

"""

import utils, os
from log import get_logger

log = get_logger()

def split_name(name: str): 
    """Splits the name and returns the first and last name, taking into account the following:
    1. Dr. / Mr. / Mrs. / Ms. / Miss - Remove the prefix
    2. Names with titles like MD, PhD - Ignored
    
    Assumes that there is no middle name, so the first and last name are side by side.

    Args:
        name (str): The name, as taken from the dataframe.
    
    Returns:
        Returns the firstname and lastname as strings, or None, None if the name is not given.
    """
    # if the row has no name
    if type(name) == float:
        return None, None

    name_split = name.split(' ')

    # handle the prefixes
    if 'Dr.' in name or 'Mr.' in name or 'Mrs.' in name or 'Ms.' in name or 'Miss' in name:
        return name_split[1], name_split[2]
    else:
        return name_split[0], name_split[1]

def process_csv(name: str):
    """Processes a CSV based on the requirements of section 1, and saves locally with the same 
    filename but with '_processed' suffix.

    This includes:
        - Split the `name` field into `first_name`, and `last_name`
        - Remove any zeros prepended to the `price` field
        - Delete any rows which do not have a `name`
        - Create a new field named `above_100`, which is `true` if the price is strictly greater than 
        100

    If the CSV is not found, then a warning is raised.

    Args:
        name (str): The name of the CSV file to process.
    """
    # load the CSV
    dataset_df = utils.get_csv(os.getcwd() + '\\data\\' + name)
    if dataset_df is None:
        log.warning('Unable to find and process file: ' + name)
        return

    # iterate through the df and process each row
    count = 0
    processed_data = []
    for index, row in dataset_df.iterrows():
        firstname, lastname = split_name(row['name'])
        if firstname is None:
            continue

        price = float(row['price'])                                         # remove prepending 0's
        processed_data.append([firstname, lastname, price, price > 100.0])

        count = count + 1

    log.info('Processed entries: ' + str(count))

    # save the new CSV file
    processed_filename = name.replace('.csv', '_processed.csv')
    processed_dir = os.getcwd() + '\\data'
    processed_columns = ['first_name', 'last_name', 'price', 'above_100']

    if utils.generate_csv(processed_dir, processed_filename, processed_data, processed_columns):
        log.info('Processed file successfully!')
    else:
        log.warn('Failed to process file.')
        
def main():
    dataset_names = ['dataset1.csv', 'dataset2.csv']
    for dataset in dataset_names:
        process_csv(dataset)

if __name__ == "__main__":
    main()
