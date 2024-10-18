FROM quay.io/astronomer/astro-runtime:12.1.1

COPY requirements.txt /usr/local/airflow/requirements.txt
RUN pip install --no-cache-dir -r /usr/local/airflow/requirements.txt
