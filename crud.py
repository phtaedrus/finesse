import csv
import pandas as pd

from pathlib import Path

FILEPATH = [f for f in Path('./data/').iterdir()]


class CustomDataFrame:

    def __init__(self, file):
        self.my_dfs = self.get_df_from_csv(file)
        # self.headers = self.get_headers(file)

    def get_df_from_csv(self, files) -> pd.DataFrame():
        data_frames = []

        for file in files:
            filename = file.name[:-4]

            with open(file) as f:
                filename_df = pd.read_csv(f, header=0, sep=',')
            data_frames.append(filename_df)

        return data_frames

"""
class Schema:
    def __init__(self):
        self.
"""

def main():
    a = CustomDataFrame(FILEPATH)
    print(a.my_dfs[0].columns)
    print(a.my_dfs[0].describe())
    print(a.my_dfs[1].columns)
    print(a.my_dfs[1].describe())
    print(a.my_dfs[2].columns)
    print(a.my_dfs[2].describe())


if __name__ == '__main__':
    main()
