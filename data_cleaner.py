import re
import os
import pandas as pd
import numpy as np
import env_params as env
from logger_master import logger, log_function_entry_exit


@log_function_entry_exit(logger)
class DataCleaner:
    def __init__(self):
        self.env = env
        self.df = None

    def load_data(self):
        processed_file = os.path.join('content', f'merged_data_regenerate_{self.env.start_year}_{self.env.end_year}.csv')
        self.df = pd.read_csv(processed_file)
        return self.df.head()

    def extract_number(self, s):
        return int(re.findall(r'\d+', s)[0])

    def drop_duplicate_trauma_columns(self):
        # Extract columns that start with 'trauma' or 'ctrauma'
        trauma_cols = sorted([col for col in self.df.columns if col.startswith('trauma')], key=self.extract_number)
        ctrauma_cols = sorted([col for col in self.df.columns if col.startswith('ctrauma')], key=self.extract_number)

        # Combine both lists
        all_trauma_cols = trauma_cols + ctrauma_cols

        # Identify pairs of columns where one ends with '.1'
        cols_to_drop = []
        for col in all_trauma_cols:
            if col.endswith('.1') and col[:-2] in all_trauma_cols:
                if self.df[col].equals(self.df[col[:-2]]):
                    cols_to_drop.append(col)

        # Drop identified duplicate columns
        self.df.drop(cols_to_drop, axis=1, inplace=True)

    def reverse_scale_columns(self):
        discrimination_cols = sorted([col for col in self.df.columns if col.startswith('discrimination')], key=self.extract_number)
        for col in discrimination_cols:
            self.df[col] = 7 - self.df[col]

    def calculate_trauma_scores(self):
        trauma_cols = sorted([col for col in self.df.columns if col.startswith('trauma')], key=self.extract_number)
        years_to_replace = [2006, 2008, 2010, 2012]

        # Replace specific values in trauma columns for certain years
        mask = self.df['year_data'].isin(years_to_replace)
        self.df.loc[mask, trauma_cols] = self.df.loc[mask, trauma_cols].replace(5, 0)
        self.df['Count_Missing'] = self.df[trauma_cols].isnull().sum(axis=1)
        self.df['trauma_score'] = self.df[trauma_cols].fillna(0).sum(axis=1)
        self.df['trauma_score'] = (self.df['trauma_score'] * len(trauma_cols)) / (len(trauma_cols) - self.df['Count_Missing'])
        self.df.loc[self.df['year_data'].isin([2014, 2016]), 'trauma_score'] = np.nan
        self.nullify_if_all_missing(trauma_cols, 'trauma_score')

    def calculate_ctrauma_scores(self):
        ctrauma_cols = sorted([col for col in self.df.columns if col.startswith('ctrauma')], key=self.extract_number)
        self.df[ctrauma_cols] = self.df[ctrauma_cols].replace({5: 0})
        self.df['ctrauma_score'] = self.df[ctrauma_cols].fillna(0).sum(axis=1)
        self.df['Count_Missing'] = self.df[ctrauma_cols].isnull().sum(axis=1)
        self.df['ctrauma_score'] = (self.df['ctrauma_score'] * len(ctrauma_cols)) / (len(ctrauma_cols) - self.df['Count_Missing'])
        self.df.loc[self.df['year_data'].isin([2014, 2016]), 'ctrauma_score'] = np.nan
        self.nullify_if_all_missing(ctrauma_cols, 'ctrauma_score')

    def calculate_series_points(self):
        serial_cols = sorted([col for col in self.df.columns if col.startswith('serial')], key=self.extract_number)
        self.df[serial_cols] = self.df[serial_cols].replace({998: 0, 999: 0})
        self.df['series_points'] = 0
        for i in range(len(serial_cols) - 1):
            self.df['series_points'] += ((self.df[serial_cols[i]] - self.df[serial_cols[i+1]] == 7) |
                                         (np.isnan(self.df[serial_cols[i]]) & (self.df[serial_cols[i+1]] == 93 - 7 * (i + 1)))).astype(int)
        self.nullify_if_all_missing(serial_cols, 'series_points')

    def calculate_backwardcount_score(self):
        def calculate_backward_points(row):
            if np.isnan(row['backwardcount-try1']):
                return np.nan
            elif row['backwardcount-try1'] == 1:
                return 2
            elif row['backwardcount-try1'] in [5, 9]:
                return 0
            elif row['backwardcount-try2'] == 1:
                return 1
            elif row['backwardcount-try2'] in [5, 9]:
                return 0
            else:
                return np.nan

        self.df['backwardcount_score'] = self.df.apply(calculate_backward_points, axis=1)

    def calculate_cognition_scores(self):
        cognition_cols = ['backwardcount_score', 'immediate10', 'delayed10', 'series_points']
        self.df['cognition_score'] = self.df[cognition_cols].fillna(0).sum(axis=1)
        self.df['cognition_score'] = 27 - self.df['cognition_score']
        self.nullify_if_all_missing(cognition_cols, 'cognition_score')

    def calculate_physical_social_scores(self):
        physical_cols = ['vandalism', 'vacancy', 'safety', 'rubbish']
        social_cols = ['belonging', 'help', 'trust', 'friendliness']
        self.calculate_score('physical_disorder_score', physical_cols)
        self.calculate_score('social_cohesion_score', social_cols)

    def calculate_score(self, score_name, cols):
        self.df[cols] = 8 - self.df[cols]
        scores = []
        for values in self.df[cols].values:
            count_nan = np.sum(np.isnan(values))
            if count_nan > 2:
                scores.append(np.nan)
            else:
                scores.append(np.sum(np.nan_to_num(values)) / (len(cols) - count_nan))
        self.df[score_name] = scores

    def map_demographics_values(self):
        self.map_column_values('sex', {1: "Male", 2: "Female"})
        self.map_column_values('race', {1: "White", 2: "Black/African American", 97: "Other", 98: "DK", 99: "RF"})
        self.map_column_values('hispanic', {1: "Hispanic", 5: "Non-Hispanic", 8: 'DK', 9: 'RF'})

        # Combine race and ethnicity into a single column
        self.df['race_ethnicity'] = self.df['hispanic'] + " " + self.df['race']

        self.map_column_values('race_ethnicity', {'Hispanic white': "Hispanic",
                                                  'Non-Hispanic Other': 'Other',
                                                  'Hispanic Other': "Hispanic",
                                                  'Hispanic Black/African American': "Hispanic",
                                                  'DK white': 'DK/RF',
                                                  'Hispanic RF': "Hispanic",
                                                  'Non-Hispanic DK': 'DK/RF',
                                                  'Non-Hispanic RF': 'DK/RF',
                                                  'DK Black/African American': 'DK/RF',
                                                  'RF white': 'DK/RF',
                                                  'Hispanic DK': "Hispanic",
                                                  'DK Other': 'Other',
                                                  'DK DK': 'DK/RF',
                                                  'RF RF': 'DK/RF',
                                                  'RF Other': 'Other'
                                                  })
        self.map_column_values('citizenship', {1: 'US Citizen', 9: np.nan, 5: 'Not US Citizen', 8: 'DK'})
        self.map_column_values('USborn', {1: 'US Born', 9: np.nan, 5: 'Not born in US'})
        self.map_column_values('genhealth', {8: np.nan, 9: np.nan})
        self.map_column_values('selfmemory', {8: np.nan, 9: np.nan})

    def map_column_values(self, col, mapping_dict):
        self.df[col] = self.df[col].replace(mapping_dict)

    def assign_cognition_category(self):
        self.df['cognition_category'] = pd.Series(dtype="string")
        self.df.loc[self.df['cognition_score'] <= 15, 'cognition_category'] = 'Normal'
        self.df.loc[self.df['cognition_score'] > 15, 'cognition_category'] = 'Not Normal'

    def save_cleaned_data(self):
        cleaned_file = os.path.join('content', f'cleaned_data_{self.env.start_year}_{self.env.end_year}.csv')
        self.df.to_csv(cleaned_file, index=False)

    def nullify_if_all_missing(self, cols_to_check, score_col):
        self.df[score_col] = self.df.apply(lambda row: None if all(pd.isnull(row[col]) for col in cols_to_check) else row[score_col], axis=1)

    def run(self):
        # Load the data
        self.load_data()
        # Drop duplicate trauma columns
        self.drop_duplicate_trauma_columns()
        # Reverse scale of certain columns
        self.reverse_scale_columns()
        # Calculate trauma and ctrauma scores
        self.calculate_trauma_scores()
        self.calculate_ctrauma_scores()
        # Replace values in serial columns and calculate series points
        self.calculate_series_points()
        # Calculate backward count score
        self.calculate_backwardcount_score()
        # Calculate cognition scores
        self.calculate_cognition_scores()
        # Calculate physical disorder and social cohesion scores
        self.calculate_physical_social_scores()
        # Map column values for demographics
        self.map_demographics_values()
        # Assign cognition category based on the 'cognition_score'
        self.assign_cognition_category()
        # Save the cleaned data
        self.save_cleaned_data()


def main():
    """instantiate and run the DataCleaner"""
    processor = DataCleaner()
    processor.run()


if __name__ == "__main__":
    main()
