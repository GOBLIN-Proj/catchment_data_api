from catchment_data_api.cohorts import Cohorts

def main():
    cohort = Cohorts("blackwater")

    print(cohort.cohorts)

    print(cohort.herd_relation_dict)
    print(cohort.compute_coef_cohort_population())

    print(cohort.compute_cohort_population_in_catchment())

    print(cohort.catchment_herd_raw)

if __name__ == "__main__":
    main()  