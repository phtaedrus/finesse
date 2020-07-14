from sqlalchemy import inspect

import ddl
import numpy as np
import pandas as pd

from pathlib import Path

#modify pandas display
pd.set_option("display.expand_frame_repr", True)
pd.set_option("display.max_rows", 30)
pd.set_option("display.max_columns", 30)

#Not really a constant but once read should stay static.
FILEPATHS = [f for f in Path('./data/').iterdir()][:]


class CustomDataFrames:
    """Creates custom data frame objects"""

    def __init__(self, file):
        self.base_dfs = self.get_df_from_csv(file)
        self.tables = []
        self.raw_df = pd.DataFrame()
        self.post_metrics_df = pd.DataFrame()
        self.hash_df = pd.DataFrame()

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

    def add_columns(self):
        """
        def add_columns() is the outside function that
        uses private helper_functions:

        -def _add_hashtag_df_columns()
        -def _add_post_metrics_df_columns()
        -def _add_raw_df_columns()

        Also updates self.pd.Dataframe() objects

        args:
        -self


        :returns:
            _add_hashtag_df_columns(hash_df)
            _add_post_metrics_df_columns(post_metrics_df)
            _add_raw_df_columns(raw_df)
        """

        hash_df, raw_df, post_metrics_df = self.base_dfs[0].copy(), \
                                           self.base_dfs[1].copy(), \
                                           self.base_dfs[2].copy()

        def _add_hashtag_df_columns(_df=hash_df):
            """returns a modified copy of hash_df: pd.Dataframe()"""

            _df['segment_id'] = _df['post_url'] \
                .str \
                .slice(start=28, stop=39)

            hash_df = _df
            return hash_df

        def _add_post_metrics_df_columns(_df=post_metrics_df):
            """returns a modified copy of post_metrics_df: pd.Dataframe()"""

            _df['segment_id'] = _df['post_url'] \
                .str \
                .slice(start=28, stop=39)

            post_metrics_df = _df

            return post_metrics_df

        def _add_raw_df_columns(_df=raw_df):
            """returns a modified copy of raw_df: pd.Dataframe()"""

            _df['segment_id'] = _df['post_url'].str.slice(start=28, stop=39)

            df = _df.reindex(columns=['post_url', 'segment_id', 'num_likes',
                                      'num_comments', 'num_views',
                                      'date_time_collected'])
            raw_df = df

            return raw_df

        self.raw_df = _add_raw_df_columns()
        self.hash_df = _add_hashtag_df_columns()
        self.post_metrics_df = _add_post_metrics_df_columns()


def load_to_sql(dfs: [pd.DataFrame]):
    """
    Loads modified pd.Dataframe() objects to sql database.

    args:
    -self, dfs: [pd.Dataframe]

    output:
    Log message
    """

    for i, df in enumerate(dfs):
        if i == 0:
            df.to_sql('top_appearances', ddl.engine,
                      if_exists='replace', index_label='id')
            print(f"Table {i} Successfully Loaded to SQL DB")
        elif i == 1:
            df.to_sql('post_metrics_and_comments', ddl.engine,
                      if_exists='replace', index_label='id')
            print(f"Table {i} Successfully Loaded to SQL DB")

        else:
            df.to_sql('raw_metrics', ddl.engine,
                      if_exists='replace', index_label='id', schema=None)
            print(f"Table {i} Successfully Loaded to SQL DB")


def main():
    df_object = CustomDataFrames(FILEPATHS)
    df_object.get_df_from_csv(FILEPATHS)
    print(df_object.tables)
    df_object.add_columns()
    load_to_sql([df_object.hash_df, df_object.raw_df, df_object.post_metrics_df])


if __name__ == '__main__':
    main()
