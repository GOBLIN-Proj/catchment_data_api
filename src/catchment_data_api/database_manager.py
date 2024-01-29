import sqlalchemy as sqa
import pandas as pd
from catchment_data_api.database import get_local_dir
import os


class DataManager:
    def __init__(self):
        self.database_dir = get_local_dir()
        self.engine = self.data_engine_creater()

    def data_engine_creater(self):
        database_path = os.path.abspath(
            os.path.join(self.database_dir, "livestock_land_cover_database")
        )
        engine_url = f"sqlite:///{database_path}"

        return sqa.create_engine(engine_url)
    
    def get_national_herd_raw(self):
        table = "2012_to_2020_herd_numbers"
        dataframe = pd.read_sql(
            "SELECT * FROM '%s'" % (table),
            self.engine,
            index_col=["Cohorts"]
        )

        dataframe.iloc[: ,1:] *= 1000

        return dataframe

    def get_catchment_livestock_data(self):
        table = "livestock_data_table"
        dataframe = pd.read_sql(
            "SELECT * FROM '%s'" % (table),
            self.engine,
        )

        return dataframe
    

    def get_catchment_forest_data(self):
        table = "forest_database_table"
        dataframe = pd.read_sql(
            "SELECT * FROM '%s'" % (table),
            self.engine,
        )

        return dataframe
    

    def get_catchment_grass_data(self):
        table = "grass_database_table"
        dataframe = pd.read_sql(
            "SELECT * FROM '%s'" % (table),
            self.engine,
        )

        return dataframe
    

    def get_catchment_cultivated_data(self):
        table = "cult_database_table"
        dataframe = pd.read_sql(
            "SELECT * FROM '%s'" % (table),
            self.engine,
        )

        return dataframe
    

    def get_catchment_peat_data(self):
        table = "peat_database_table"
        dataframe = pd.read_sql(
            "SELECT * FROM '%s'" % (table),
            self.engine,
        )

        return dataframe
    

    def get_catchment_lucas_data(self):
        table = "lucas_database_table"
        dataframe = pd.read_sql(
            "SELECT * FROM '%s'" % (table),
            self.engine,
        )

        return dataframe