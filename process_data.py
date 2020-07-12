

import ddl
import csv
import numpy as np
import pandas as pd

from pathlib import Path


FILEPATHS = [f for f in Path('./data/').iterdir()]


class CustomDataFrame:
    """Creates custom data frame objects"""

    def __init__(self, file):
        self.my_dfs = self.get_df_from_csv(file)
        self.tables = []


    def get_df_from_csv(self, files) -> pd.DataFrame():
        """ """

        data_frames, table_names = [], []

        for file in files:
            df_name = file.name[:-4]
            table_names.append(df_name)
            with open(file) as f:
                filename_df = pd.read_csv(f, header=0, sep=',')
            data_frames.append(filename_df)

            self.tables = table_names

        return data_frames


def main():
    a = CustomDataFrame(FILEPATHS)
    #print(a.my_dfs[0].columns)
    #print(a.my_dfs[0].describe())
    #print(a.my_dfs[1].columns)
    #print(a.my_dfs[1].describe())
    #print(a.my_dfs[2].columns)
    #print(a.my_dfs[2].describe())
    b = ddl.RawMetrics()
    print(b)


if __name__ == '__main__':
    main()
