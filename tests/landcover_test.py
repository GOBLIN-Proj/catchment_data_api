from catchment_data_api import catchment_data_api
from catchment_data_api.crops import Crops

def main():
    api = catchment_data_api.CatchmentDataAPI()

    df = api.get_catchment_peat_data_by_catchment_name("Cork Harbour")

    print(df)

    df1 = api.get_catchment_msa_data_by_catchment_name("Cork Harbour")

    print(f"MSA data for Cork Harbour: {df1}")


if __name__ == "__main__":
    main()
