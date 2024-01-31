import pandas as pd
from catchment_data_api.catchment_data_api import CatchmentDataAPI

class Crops:
    def __init__(self):
        self.api = CatchmentDataAPI()


    def _derive_crops(self, catchment):
       lucas_df = self.api.get_catchment_lucas_data_by_catchment_name(catchment)
       cultivated_df = self.api.get_catchment_cultivated_data_by_catchment_name(catchment)

       #Assume crops are mineral 
       grouped_cultivated_df = cultivated_df.groupby(['cover_type']).sum()

       total_cultivated_land_area = grouped_cultivated_df['total_hectares'].sum()

       data =[]

       for crop in lucas_df['crop_type'].unique():
            row = {
                "catchment":self.api.format_catchment_name(catchment),
                "crop":crop,
                "area_ha":total_cultivated_land_area * lucas_df.loc[lucas_df['crop_type'] == crop]['crop_proportion'].item()
            }

            data.append(row)

       return pd.DataFrame(data)
    

    def get_catchment_crops(self, catchment):
        df = self._derive_crops(catchment)

        return df