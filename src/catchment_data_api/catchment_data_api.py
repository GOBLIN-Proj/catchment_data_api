import pandas as pd 
import re
from catchment_data_api.database_manager import DataManager
from catchment_data_api.static_data import StaticData

class CatchmentDataAPI:
    def __init__(self):
        self.data_manager = DataManager()
        self.static_data = StaticData()
        self.known_catchments = self.get_catchment_names()

    def normalize_text(self, text):
        # Lowercase, remove special characters, replace &/and
        text = text.lower()
        text = re.sub(r'\W+', ' ', text)
        text = text.replace(' & ', ' and ')
        return text


    def format_catchment_name(self, catchment_name):

        normalized_input = self.normalize_text(catchment_name)
        input_words = set(normalized_input.split())

        best_match = None
        highest_word_match_count = 0

        for known_catchment in self.known_catchments:
            normalized_catchment = self.normalize_text(known_catchment)
            catchment_words = set(normalized_catchment.split())

            common_words_count = len(input_words.intersection(catchment_words))

            if common_words_count > highest_word_match_count:
                highest_word_match_count = common_words_count
                best_match = known_catchment

        return best_match if best_match else catchment_name


    def get_catchment_names(self):

        df = self.data_manager.get_catchment_livestock_data()
        catchment_names = df['Catchment'].unique()
        return catchment_names
    

    def get_national_herd_raw(self):
        df = self.data_manager.get_national_herd_raw()
        return df

    def get_catchment_livestock_data(self):
        df = self.data_manager.get_catchment_livestock_data()
        return df


    def get_catchment_livestock_data_by_catchment_name(self, catchment_name):

        catchment = self.format_catchment_name(catchment_name)

        df = self.data_manager.get_catchment_livestock_data()

        catchment_data = df[df['Catchment'] == catchment]

        return catchment_data


    def get_catchment_livestock_total_pop_by_catchment_name(self, catchment_name):

        # Format the catchment name to ensure consistency
        catchment = self.format_catchment_name(catchment_name)

        # Retrieve the full dataset
        df = self.data_manager.get_catchment_livestock_data()

        # Group by the 'Catchment' column and sum up the populations
        grouped_data = df.groupby('Catchment').sum(numeric_only=True)

        # Check if the specified catchment exists and create a DataFrame
        if catchment in grouped_data.index:
            sheep_population = int(grouped_data.loc[catchment, 'Sheep pop'])
            upland_ewes_split = self.static_data.get_ewe_split_dict()['Upland ewes']
            lowland_ewes_split = self.static_data.get_ewe_split_dict()['Lowland ewes']

            catchment_data = pd.DataFrame({
                'Catchment': [catchment],
                'dairy_cows': [int(grouped_data.loc[catchment, 'Dairy pop'])],
                'suckler_cows': [int(grouped_data.loc[catchment, 'Beef pop'])],
                'Upland ewes': [int(sheep_population * upland_ewes_split)],
                'Lowland ewes': [int(sheep_population * lowland_ewes_split)]
            })
        else:

            # If catchment is not found, return an empty DataFrame with the same columns
            catchment_data = pd.DataFrame(columns=['Catchment', 'Dairy pop', 'Beef pop', 'Sheep pop'])

        return catchment_data


    def get_catchment_forest_data(self):
        df = self.data_manager.get_catchment_forest_data()
        return df
    

    def get_catchment_grass_data(self):
        df = self.data_manager.get_catchment_grass_data()
        return df
    

    def get_catchment_cultivated_data(self):
        df = self.data_manager.get_catchment_cultivated_data()
        return df
    

    def get_catchment_peat_data(self):
        df = self.data_manager.get_catchment_peat_data()
        return df   
    

    def get_catchment_lucas_data(self):
        df = self.data_manager.get_catchment_lucas_data()
        return df
    

    def get_catchment_grass_in_use(self):
        df = self.data_manager.get_catchment_grass_data()
        
        mask = (df["cover_type"] == "Improved Grassland") | (df["cover_type"] == "Wet Grassland") | (df["cover_type"] == "Dry Grassland")

        grass_df = df.loc[mask]

        return grass_df


    def get_formatted_catchment_grass_in_use(self):
        df = self.get_catchment_grass_in_use()

        # Create a pivot table with MultiIndex columns
        grouped_data = df.pivot_table(index='catchment',
                                    columns=['cover_type', 'soil_type'],
                                    values='total_hectares',
                                    aggfunc='sum',
                                    fill_value=0)

        # Identify unique soil types
        soil_types = df['soil_type'].unique()

        # For each soil type, create 'Pasture' and 'Rough_grazing_in_use' columns
        for soil_type in soil_types:
            grouped_data[('Pasture', soil_type)] = grouped_data[('Improved Grassland', soil_type)]
            grouped_data[('Rough_grazing_in_use', soil_type)] = (
                grouped_data[('Wet Grassland', soil_type)] + grouped_data[('Dry Grassland', soil_type)]
            )

        # Drop the original grassland type columns for each soil type
        for soil_type in soil_types:
            for grassland_type in ['Improved Grassland', 'Wet Grassland', 'Dry Grassland']:
                if (grassland_type, soil_type) in grouped_data.columns:
                    grouped_data.drop(columns=(grassland_type, soil_type), inplace=True)

        # Reset index if required
        grouped_data.reset_index(inplace=True)

        return grouped_data


    def get_catchment_grass_data_by_catchment_name(self, catchment_name):

        catchment = self.format_catchment_name(catchment_name)

        df = self.get_formatted_catchment_grass_in_use()

        catchment_data = df[df['catchment'] == catchment]

        return catchment_data