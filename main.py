import ddl
import etl
from process_data import *


def main():
    df_object = CustomDataFrames(FILEPATHS)
    df_object.get_df_from_csv(FILEPATHS)

    # print(df_object.hash_df)

    normalize_table_one = NormalizeDataService(df_object.base_dfs[0],
                                                      'hashtag_top_appearances')
    normalize_table_one.add_df_columns()
    normalize_table_one.load_to_sql()

    normalize_table_two = NormalizeDataService(df_object.base_dfs[1],
                                               'post_metrics_and_comments')
    normalize_table_two.add_df_columns()
    normalize_table_two.load_to_sql()

    normalize_table_three = NormalizeDataService(df_object.base_dfs[2],
                                                 'raw_post_metrics')
    normalize_table_three.add_df_columns()
    normalize_table_three.load_to_sql()

if __name__ == '__main__':
    main()
