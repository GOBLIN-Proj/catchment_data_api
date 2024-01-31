from catchment_data_api import catchment_data_api
from catchment_data_api.crops import Crops

def main():
    api = catchment_data_api.CatchmentDataAPI()

    df = api.get_catchment_lucas_data_by_catchment_name("blackwater")

    print(df)

    crops = Crops()

    df1 = crops._derive_crops("blackwater")

    print(df1)

if __name__ == "__main__":
    main()
