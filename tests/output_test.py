from catchment_data_api import catchment_data_api
import unittest
import os
from tempfile import TemporaryDirectory

class TestGenerateScenarioDataFrame(unittest.TestCase):
    def test_generate_scenario_dataframe_creates_file(self):
        # Use a temporary directory
        with TemporaryDirectory() as tmp_dir:
            api = catchment_data_api.CatchmentDataAPI()

            # Define the path to the test data
            expected_file_name = "catchment_livestock.csv"
            expected_file_path = os.path.join(tmp_dir, expected_file_name)

            api.get_catchment_livestock_data().to_csv(expected_file_path)


            # Check if the file was created as expected
            self.assertTrue(os.path.exists(expected_file_path), f"File {expected_file_name} was not created in temporary directory.")

            #Define the path to the test data
            expected_file_name = "catchment_livestock_by_name.csv"
            expected_file_path = os.path.join(tmp_dir, expected_file_name)

            api.get_catchment_livestock_data_by_catchment_name("blackwater").to_csv(expected_file_path)

            # Check if the file was created as expected
            self.assertTrue(os.path.exists(expected_file_path), f"File {expected_file_name} was not created in temporary directory.")

            #Define the path to the test data
            expected_file_name = "catchment_livestock_total_pop_by_name.csv"
            expected_file_path = os.path.join(tmp_dir, expected_file_name)

            api.get_catchment_livestock_total_pop_by_catchment_name("blackwater").to_csv(expected_file_path)

            # Check if the file was created as expected
            self.assertTrue(os.path.exists(expected_file_path), f"File {expected_file_name} was not created in temporary directory.")

            #Define the path to the test data
            expected_file_name = "catchment_lucas_by_name.csv"
            expected_file_path = os.path.join(tmp_dir, expected_file_name)

            api.get_catchment_lucas_data_by_catchment_name("blackwater").to_csv(expected_file_path)

            # Check if the file was created as expected
            self.assertTrue(os.path.exists(expected_file_path), f"File {expected_file_name} was not created in temporary directory.")

            #Define the path to the test data
            expected_file_name = "catchment_grass.csv"
            expected_file_path = os.path.join(tmp_dir, expected_file_name)

            api.get_catchment_grass_data().to_csv(expected_file_path)

            # Check if the file was created as expected
            self.assertTrue(os.path.exists(expected_file_path), f"File {expected_file_name} was not created in temporary directory.")

            #Define the path to the test data
            expected_file_name = "catchment_grass_in_use.csv"

            expected_file_path = os.path.join(tmp_dir, expected_file_name)

            api.get_catchment_grass_in_use().to_csv(expected_file_path)

            # Check if the file was created as expected
            self.assertTrue(os.path.exists(expected_file_path), f"File {expected_file_name} was not created in temporary directory.")

            #Define the path to the test data
            expected_file_name = "formatted_catchment_grass_in_use.csv"
            expected_file_path = os.path.join(tmp_dir, expected_file_name)

            api.get_formatted_catchment_grass_in_use().to_csv(expected_file_path)

            # Check if the file was created as expected
            self.assertTrue(os.path.exists(expected_file_path), f"File {expected_file_name} was not created in temporary directory.")

            #Define the path to the test data
            expected_file_name = "catchment_grass_by_name.csv"
            expected_file_path = os.path.join(tmp_dir, expected_file_name)

            api.get_catchment_grass_data_by_catchment_name("blackwater").to_csv(expected_file_path)

            # Check if the file was created as expected
            self.assertTrue(os.path.exists(expected_file_path), f"File {expected_file_name} was not created in temporary directory.")

            #Define the path to the test data
            expected_file_name = "forest_data.csv"
            expected_file_path = os.path.join(tmp_dir, expected_file_name)

            api.get_catchment_forest_data().to_csv(expected_file_path)

            # Check if the file was created as expected
            self.assertTrue(os.path.exists(expected_file_path), f"File {expected_file_name} was not created in temporary directory.")

            #Define the path to the test data
            expected_file_name = "catchment_forest_data_by_name.csv"
            expected_file_path = os.path.join(tmp_dir, expected_file_name)

            api.get_catchment_forest_data_by_catchment_name("blackwater").to_csv(expected_file_path)

            # Check if the file was created as expected
            self.assertTrue(os.path.exists(expected_file_path), f"File {expected_file_name} was not created in temporary directory.")

            #Define the path to the test data
            expected_file_name = "catchment_peat.csv"
            expected_file_path = os.path.join(tmp_dir, expected_file_name)

            api.get_catchment_peat_data().to_csv(expected_file_path)

            # Check if the file was created as expected
            self.assertTrue(os.path.exists(expected_file_path), f"File {expected_file_name} was not created in temporary directory.")
                                                 

# Running the tests
if __name__ == '__main__':
    unittest.main()
