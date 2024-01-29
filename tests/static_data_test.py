from catchment_data_api.static_data import StaticData

def main():
    static_data = StaticData()
    herd_relation_dict = static_data.get_herd_relation_dict()
    print(herd_relation_dict)

    ewe_split_dict = static_data.get_ewe_split_dict()
    print(ewe_split_dict)

    print(static_data.get_baseline_year())

if __name__ == "__main__":
    main()