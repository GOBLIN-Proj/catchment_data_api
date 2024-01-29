from catchment_data_api import catchment_data_api

def main():
    api = catchment_data_api.CatchmentDataAPI()
    df = api.get_catchment_livestock_data()

    print(df.head())

    df1 = api.get_catchment_livestock_data_by_catchment_name("ballyteigue Bannow")

    print(df1.head())

    print(api.get_catchment_names())

    df2 = api.get_catchment_livestock_total_pop_by_catchment_name("blackwater")

    print(df2.head())



if __name__ == "__main__":
    main()
