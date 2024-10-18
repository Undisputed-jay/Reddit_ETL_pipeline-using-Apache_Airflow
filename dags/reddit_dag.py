from airflow import DAG
from datetime import datetime
from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator
from include.pipelines.reddit_pipeline import reddit_pipeline
from include.pipelines.aws_pipeline import upload_s3_pipeline
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator
from include.utils.constants import *
import os

# Define the file postfix globally to reuse it inside the tasks
file_postfix = datetime.now().strftime("%Y%m%d")

# DAG definition
@dag(
    tags=["reddit", "etl", "pipeline"],
    schedule=None,  
    catchup=False,
    default_args={
        "owner": "Ahmed Ayodele",
        "start_date": datetime(2024, 10, 17)
    },
    template_searchpath=['/usr/local/airflow/include'],
)
def etl_reddit_pipeline():
    # Task to extract data from Reddit
    extract = PythonOperator(
        task_id = 'reddit_extraction',
        python_callable = reddit_pipeline,
        op_kwargs = {
            'file_name': f'reddit_{file_postfix}',
            'subreddit': 'dataengineering',
            'time_filter': 'day',
            'limit': 300
        }
    )

    # Task to upload data to S3 
    upload_to_aws_s3 = PythonOperator(
        task_id = 's3_upload',
        python_callable = upload_s3_pipeline,
        op_kwargs = {
            'file_path': "{{ ti.xcom_pull(task_ids='reddit_extraction') }}", # This pulls file path from previous task
            'bucket_name': AWS_BUCKET,
            'key': f"reddit_{file_postfix}.csv"
        }
    )

    load_to_redshift = S3ToRedshiftOperator(
        task_id='load_to_redshift',
        schema = 'public',           # Your Redshift schema
        table = 'reddit_data',             # Your Redshift table
        s3_bucket=AWS_BUCKET,
        s3_key=f"raw/reddit_{file_postfix}.csv", # S3 key from previous task
        copy_options=['CSV', 'IGNOREHEADER 1', 'EMPTYASNULL'],                    # Change to appropriate file format
        redshift_conn_id='redshift_conn',     # Airflow connection ID for Redshift
        aws_conn_id = 's3_conn',               # Airflow connection ID for AWS
        method='APPEND'                          # Choose APPEND or REPLACE based on your needs
    )

    # Setting task dependencies
    extract >> upload_to_aws_s3 >> load_to_redshift

# DAG instantiation
etl_dag = etl_reddit_pipeline()
