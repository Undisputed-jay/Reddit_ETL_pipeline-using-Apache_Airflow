import configparser
import os

# Initialize the parser
parser = configparser.ConfigParser()

# Build the config file path
config_path = os.path.join(os.environ.get('AIRFLOW_HOME', '/usr/local/airflow'), 'config/config.conf')

# Read the config file
parser.read(config_path)

# Get values from the config file
SECRET = parser.get('api_keys', 'reddit_secret_key')
CLIENT_ID = parser.get('api_keys', 'reddit_client_id')

DATABASE_HOST = parser.get('database', 'database_host')
DATABASE_NAME = parser.get('database', 'database_name')
DATABASE_PORT = parser.get('database', 'database_port')
DATABASE_USER = parser.get('database', 'database_username')
DATABASE_PASSWORD = parser.get('database', 'database_password')


AWS_ACCESS_KEY_ID = parser.get('aws', 'aws_access_key')
AWS_SECRET_KEY = parser.get('aws', 'aws_secret_access_key')
AWS_REGION = parser.get('aws', 'aws_region')
AWS_BUCKET = parser.get('aws', 'aws_bucket')

INPUT_PATH = os.path.join(os.environ.get('AIRFLOW_HOME', '/usr/local/airflow'), 'include/data/input')
OUTPUT_PATH = os.path.join(os.environ.get('AIRFLOW_HOME', '/usr/local/airflow'), 'include/data/output')

POST_FIELDS = (
    'id',
    'title',
    'selftext',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'upvote_ratio',
    'over_18',
    'edited',
    'spoiler',
    'stickied',
)