from airflow.providers.amazon.aws.hooks.s3 import S3Hook

def upload_s3_pipeline(file_path: str, key: str, bucket_name: str) -> None:
    hook = S3Hook(aws_conn_id="s3_conn")
    raw_key = f"raw/{key}"
    hook.load_file(filename = file_path, key = raw_key, bucket_name = bucket_name)
    

#/usr/local/airflow/include/data/output/reddit_20241015.csv
#return_value
