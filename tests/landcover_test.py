from catchment_data_api import catchment_data_api
from catchment_data_api.crops import Crops

def main():
    api = catchment_data_api.CatchmentDataAPI()

    df = api.get_catchment_peat_data_by_catchment_name("Cork Harbour")

    print(df)


if __name__ == "__main__":
    main()
