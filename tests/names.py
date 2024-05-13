from catchment_data_api.catchment_data_api import CatchmentDataAPI

def main():
    api = CatchmentDataAPI()
    print(api.format_catchment_name("Lee, Cork Harbour and Youghal Bay"))

if __name__ == "__main__":
    main()