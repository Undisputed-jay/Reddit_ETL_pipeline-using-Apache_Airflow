import pandas as pd
import os
from ..utils.constants import *
from include.etl.reddit_etl import *

def reddit_pipeline(file_name: str, subreddit: str, time_filter: str = 'day', limit = None):
    #connect to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')
    #extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    #transformation
    post_df = transform_data(post_df)
    #data to csv
    file_path = os.path.join(OUTPUT_PATH, f'{file_name}.csv')
    load_data_to_csv(post_df, file_path)

    return file_path