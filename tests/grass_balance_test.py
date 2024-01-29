import unittest
from catchment_data_api import catchment_data_api
import pandas as pd

class TestCatchmentGrassData(unittest.TestCase):
    def setUp(self):
        # Assuming you have a setup method to initialize your data API
        self.api = catchment_data_api.CatchmentDataAPI()

    def test_total_area_per_catchment(self):
        # Get the original data
        original_df = self.api.get_catchment_grass_in_use()

        # Get the formatted data
        formatted_df = self.api.get_formatted_catchment_grass_in_use()

        # Summarize the total area for each catchment in original data
        total_area_original = original_df.groupby('catchment')['total_hectares'].sum()

        # Summarize the total area for each catchment in formatted data
        # 'Pasture' and 'Rough_grazing_in_use' columns need to be summed across all soil types
        formatted_df['Total_Area'] = formatted_df.filter(like='Pasture').sum(axis=1) + formatted_df.filter(like='Rough_grazing_in_use').sum(axis=1)
        total_area_formatted = formatted_df.groupby('catchment')['Total_Area'].sum()

        # Compare the total areas for each catchment
        pd.testing.assert_series_equal(total_area_original, total_area_formatted, check_names=False)

if __name__ == '__main__':
    unittest.main()
