<html lang="en">
<head>
    <title>Reddit ETL Data Engineering Pipeline</title>
</head>
<body>
    <h1>Reddit ETL Data Engineering Pipeline</h1>
    <p><strong>Reddit ETL Data Engineering Pipeline</strong> is an automated workflow designed to extract, transform, and load Reddit data, specifically from the "dataengineering" subreddit. The pipeline is built using Apache Airflow, facilitating task scheduling and orchestration. It features the following steps:</p>
    <ul>
        <li><strong>Reddit Data Extraction</strong>: A Python script pulls data from Reddit, filtering posts by the "day" time range and limiting the extraction to 300 posts. The extracted data is saved locally in a specified file format.</li>
        <li><strong>Upload to AWS S3</strong>: The extracted data is then uploaded to an Amazon S3 bucket for storage and further processing.</li>
        <li><strong>Load to Redshift</strong>: After storage in S3, the data is transferred to Amazon Redshift for analytics and reporting. The data is copied into a Redshift table using the S3ToRedshiftOperator.</li>
    </ul>
    <p>This pipeline ensures seamless data extraction and storage, making the Reddit data accessible for further analysis and insights within a scalable, cloud-based environment.</p>
</body>
</html>
