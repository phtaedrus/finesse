
import ddl
import numpy as np
import pandas as pd

from pathlib import Path

# modify pandas display
pd.set_option("display.expand_frame_repr", True)
pd.set_option("display.max_rows", 30)
pd.set_option("display.max_columns", 30)

# Not really a constant but once read should stay static.
FILEPATHS = [f for f in Path('./data/').iterdir()][:]


class CustomDataFrames:
    """Creates custom data frame objects"""

    def __init__(self, file):
        self.base_dfs = self.get_df_from_csv(file)
        self.tables = []
        #self.hash_df = self.base_dfs[0]  # needs refactored
        # self.post_metrics_df = self.base_dfs[1]  # needs refactored
        # self.raw_df = self.base_dfs[0]  # needs refactored

    def get_df_from_csv(self, files) -> pd.DataFrame():
        """
        Processes flat files and loads the data into a pandas dataframe.
        Also updates the self.tables list.

        args:
        -self, files

        output:
        list of pd.Dataframe() objects
        """

        data_frames, table_names = [], []

        for file in files:
            table_names.append(file.name[:-4])
            index = pd.Index
            with open(file) as f:
                filename_df = pd.read_csv(f, header=0, sep=',', index_col=None) \
                    .rename_axis('id') \
                    .fillna(np.nan)

            data_frames.append(filename_df)
            self.tables = table_names

        return data_frames


class NormalizeDataService(CustomDataFrames):

    def __init__(self, df, df_name):
        super().__init__(file=FILEPATHS)
        self.df = df
        self.df_name = df_name

    def add_df_columns(self):
        """returns a modified copy of hash_df: pd.Dataframe()"""
        _df = self.df.copy()

        try:
            _df['segment_id'] = _df['post_url'] \
                .str \
                .slice(start=28, stop=39)
        except:
            pass

        self.df = _df
        return self.df

    def load_to_sql(self):
        """
        Loads modified pd.Dataframe() objects to sql database.

        args:
        -self, dfs: [pd.Dataframe]

        output:
        Log message
        """
        df = self.df
        df.to_sql(self.df_name, ddl.engine, if_exists='replace', index_label='id')

        print(f"Table {self.df_name} successfully loaded to SQL DB")

        return
