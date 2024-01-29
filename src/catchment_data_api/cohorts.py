import numpy as np
import pandas as pd
from catchment_data_api.catchment_data_api import CatchmentDataAPI
from catchment_data_api.static_data import StaticData


class Cohorts:
    def __init__(self, catchment_name):
        self.api = CatchmentDataAPI()
        self.static_data = StaticData()
        self.baseline_year = self.static_data.get_baseline_year()
        self.national_herd_raw = self.api.get_national_herd_raw()
        self.catchment_herd_raw = self.api.get_catchment_livestock_total_pop_by_catchment_name(catchment_name)
        self.herd_relation_dict = self.api.static_data.get_herd_relation_dict()
        self.cohorts = self.get_cohorts()
        self.coef = self.compute_coef_cohort_population()


    def get_cohorts(self):
        """
        Produced a dictionary of cohorts, with their populations as values
        """

        cohorts = {}

        for index, row in self.national_herd_raw.loc[:, str(self.baseline_year)].items():

            if index not in cohorts.keys():
                cohorts[index] = row

            else:
                cohorts[index] += row

        return cohorts


    def compute_coef_cohort_population(self):
        """
        sums the beef and dairy adult population, and sheep. The individual cohorts are divided
        by the result to give the cohort coef.
        """

        coef = {}
        for animal_type in ["Cattle", "Sheep"]:
            herd_dict = self.herd_relation_dict[animal_type]

            for cohort_index in herd_dict.keys():

                coef[cohort_index] = self.cohorts[cohort_index] / np.sum(
                    [self.cohorts[i] for i in herd_dict[cohort_index]], axis=0
                )

        return coef
    

    def compute_cohort_population_in_catchment(self):

        cattle_list = ["dairy_cows", "suckler_cows"] + list(self.herd_relation_dict["Cattle"].keys())
        sheep_list = ["Upland ewes", "Lowland ewes"] + list(self.herd_relation_dict["Sheep"].keys())

        _catchment_herd_cattle = pd.DataFrame(
            0, index=[self.baseline_year], columns=cattle_list
        )
        _catchment_herd_sheep = pd.DataFrame(
            0, index=[self.baseline_year], columns=sheep_list
        )

        for animal_type in ["Cattle", "Sheep"]:
            if animal_type == "Cattle":
                for cohort in cattle_list:
                    if cohort in self.herd_relation_dict[animal_type].keys():

                        _catchment_herd_cattle[cohort] = np.sum(
                            [
                                self.coef[cohort] * self.catchment_herd_raw[i]
                                for i in self.herd_relation_dict[animal_type][cohort]
                            ],
                            axis=0,
                        )

                    else:
                        _catchment_herd_cattle[
                            cohort
                        ] = self.catchment_herd_raw[cohort].values[0]

            elif animal_type == "Sheep":

                for cohort in sheep_list:

                    if cohort in self.herd_relation_dict[animal_type].keys():

                        _catchment_herd_sheep[cohort] = np.sum(
                            [
                                self.coef[cohort] * self.catchment_herd_raw[i]
                                for i in self.herd_relation_dict[animal_type][cohort]
                            ],
                            axis=0,
                        )

                    else:
                        _catchment_herd_sheep[
                            cohort
                        ] = self.catchment_herd_raw[cohort].values[0]

        return pd.concat([_catchment_herd_cattle, _catchment_herd_sheep], axis=1)

        
