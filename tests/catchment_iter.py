from catchment_data_api import catchment_data_api
from catchment_data_api.crops import Crops
import pandas as pd
import os

def main():
    api = catchment_data_api.CatchmentDataAPI()

    crop_api = Crops()

    path ="./data/"
    catchment_names = pd.read_csv(os.path.join(path, "catchment_names.csv"))

    for name in catchment_names["Catchment"]:

        print(name)
        print("PEAT")
        print(api.get_catchment_peat_data_by_catchment_name(name))
        print("#"*50)
        print("GRASS")
        print(api.get_catchment_grass_data_by_catchment_name(name))
        print("#"*50)
        print("CULTIVATED")
        print(api.get_catchment_cultivated_data_by_catchment_name(name))
        print("#"*50)
        print("FOREST")
        print(api.get_catchment_forest_data_by_catchment_name(name))
        print("#"*50)
        print("LUCAS")
        print(crop_api.get_catchment_crops(name))
        print("#"*50)

        
if __name__ == "__main__":
    main()