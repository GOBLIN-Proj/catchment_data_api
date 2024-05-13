from catchment_data_api import catchment_data_api
import pandas as pd
import os

def main():
    api = catchment_data_api.CatchmentDataAPI()

    path ="./data/"
    catchment_names = pd.read_csv(os.path.join(path, "catchment_names.csv"))

    for name in catchment_names["Catchment"]:

        print(name)
        print(api.get_catchment_peat_data_by_catchment_name(name))
        print("#"*50)
        print(api.get_catchment_grass_data_by_catchment_name(name))
        print("#"*50)
        print(api.get_catchment_cultivated_data_by_catchment_name(name))
        print("#"*50)
        print(api.get_catchment_forest_data_by_catchment_name(name))
        print("#"*50)

        



if __name__ == "__main__":
    main()