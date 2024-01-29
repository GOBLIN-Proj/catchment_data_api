from catchment_data_api import catchment_data_api

def main():
    api = catchment_data_api.CatchmentDataAPI()

    df = api.get_catchment_grass_data()

    #print(df.head(50))

    df1 = api.get_catchment_grass_in_use()

    #print(df1.head(50))

    df2 = api.get_formatted_catchment_grass_in_use()

    #print(df2.head(50))

    df3 = api.get_catchment_grass_data_by_catchment_name("blackwater")

    print(df3)

if __name__ == "__main__":
    main()
