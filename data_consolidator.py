import os
import datetime
import pyreadstat
import pandas as pd
import env_params as env
from logger_master import logger, log_function_entry_exit


@log_function_entry_exit(logger)
class DataConsolidator:
    """
    The DataConsolidator class is designed to automate the process of reading, cleaning, transforming, and consolidating
    data from multiple .sav files for a range of years. The configuration for each year.

    Steps:
    1 Get configuration for each year, including file paths, column names, and specific prefixes from the env params
    2 Read and process each year's .sav file: Load data, standardize columns, filter columns by year-specific criteria.
    3 Clean and transform the data: Rename columns per mapping, add age, and standardize the structure across years.
    4 Save the processed data for each year into a CSV file.
    5 Compile all processed yearly data into a single DataFrame and save as merged CSV file, creating a unified dataset.
    """
    def __init__(self):
        """load env params"""
        self.env = env

    def clean_df(self, df, old_column_names, new_column_names, year):
        """Cleans and transforms a DataFrame by select and rename specific columns, and adding age year fields"""
        df = df[old_column_names]
        df = df.rename(columns=dict(zip(old_column_names, new_column_names)))
        df['age'] = year - df['birthyear']
        df['year_data'] = int(year)
        return df

    def process_year_data(self, year):
        """
        Processes data for a given year.The function reads the .sav file specified for the year,
        cleans the data, and saves the processed data to a CSV file.
        """
        # get file path, prefix, and column names for the given year from the environment configuration.
        file_path = self.env.mapping_dict[year]['file']
        prefix = self.env.mapping_dict[year]['prefix']
        needed_col = self.env.mapping_dict[year]['needed_col']
        rename_col = self.env.mapping_dict[year]['rename_col']

        # Load .sav data using pyreadstat.
        df, _ = pyreadstat.read_sav(file_path)
        df.columns = df.columns.str.upper()

        # Create a list of columns needed for processing, excluding any that end with pattern 'D122'.
        new_needed_col = [col for col in needed_col if not col.endswith(prefix + 'D122')]

        # Remove the 'backwardcount' column from the renaming list if it exists.
        if 'backwardcount' in rename_col:
            rename_col.remove('backwardcount')

        # Add additional columns required for the year (e.g., 'D124' and 'D129' with the year-specific prefix)
        new_needed_col.extend([prefix + 'D124', prefix + 'D129'])
        rename_col.extend(['backwardcount-try1', 'backwardcount-try2'])

        # Clean and transform the DataFrame
        new_df = self.clean_df(df, new_needed_col, rename_col, year)

        # Save the processed DataFrame to a CSV file
        processed_file = os.path.join('content', f'rand_{year}_single_file_extract.csv')
        new_df.to_csv(processed_file, index=False)
        self.env.mapping_dict[year]['processed_file'] = processed_file

    def consolidate_data(self):
        """Consolidates processed data from multiple years into a single file"""
        print('  ', datetime.datetime.now(), f'Consolidate data - START')
        data_frames = []
        for year in range(self.env.start_year, self.env.end_year + 1, 2):
            processed_file = self.env.mapping_dict[year]['processed_file']
            data_frames.append(pd.read_csv(processed_file))
        processed_file = os.path.join('content', f'merged_data_regenerate_{self.env.start_year}_{self.env.end_year}.csv')
        consolidated_df = pd.concat(data_frames, axis=0, ignore_index=True)
        consolidated_df.to_csv(processed_file, index=False)
        print('  ', datetime.datetime.now(), f'Consolidate data - END')

    def process_sav_files(self):
        """Processes .sav files for each year in the specified range"""
        print('  ', datetime.datetime.now(), f'Processing data - START')
        for year in range(self.env.start_year, self.env.end_year+1, 2):
            print('    ', datetime.datetime.now(), f'Processing data for year: {year}')
            self.process_year_data(year)
        print('  ', datetime.datetime.now(), f'Processing data - END')

    def run(self):
        """The controller function to run the data processing and consolidation"""
        print(datetime.datetime.now(), f'DataConsolidator- START')
        self.process_sav_files()
        self.consolidate_data()
        print(datetime.datetime.now(), f'DataConsolidator - END')


def main():
    """instantiate and run the DataConsolidator"""
    processor = DataConsolidator()
    processor.run()


if __name__ == "__main__":
    main()
