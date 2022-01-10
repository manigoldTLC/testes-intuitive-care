import pandas as pd
from utils import create_dataframe, tranform_dataframe, convert_to_csv


files_2019 = [
    "2019/1T2019.csv",
    "2019/2T2019.csv",
    "2019/3T2019.csv",
    "2019/4T2019.csv",
]
files_2020 = [
    "2020/1T2020.csv",
    "2020/2T2020.csv",
    "2020/3T2020.csv",
    "2020/4T2020.csv",
]

dataframe_2019 = create_dataframe(files_2019)
dataframe_2020 = create_dataframe(files_2020)

clean_df_2019 = tranform_dataframe(dataframe_2019)
clean_df_2020 = tranform_dataframe(dataframe_2020)


full_table_2019 = pd.concat(clean_df_2019, axis=0, ignore_index=True, join="inner")
full_table_2020 = pd.concat(clean_df_2020, axis=0, ignore_index=True, join="inner")

convert_to_csv(full_table_2019, "full_table_2019")
convert_to_csv(full_table_2020, "full_table_2020")
