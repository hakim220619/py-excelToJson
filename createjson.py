import pandas
import numpy as np

excel_data_df = pandas.read_excel('kosakata english.xlsx', sheet_name='Sheet1', index_col=None)
print(excel_data_df)
excel_data_df.to_json('new_file1.json', orient='records',  force_ascii=False)

# print(json_str)