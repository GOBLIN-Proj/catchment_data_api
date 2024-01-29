import pandas as pd
from catchment_data_api.database_manager import DataManager

def main():

    data_manager = DataManager()
    df = data_manager.get_catchment_livestock_data()
    print(df.head())

if __name__ == "__main__":
    main()