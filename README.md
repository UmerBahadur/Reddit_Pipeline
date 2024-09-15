Reddit Data Engineering Pipeline with Reddit API, Airflow, Celery, Postgres, S3, AWS Glue, Athena, and Redshift.

This project provides a comprehensive data pipeline solution to extract, transform, and load (ETL) Reddit data into a Redshift data warehouse.
The pipeline leverages a combination of tools and services including Apache Airflow, Celery, PostgreSQL, Amazon S3, AWS Glue, Amazon Athena, and Amazon Redshift.


Overview
The pipeline is designed to:

Extract data from Reddit using its API.
Store the raw data into an S3 bucket from Airflow.
Transform the data using AWS Glue and Amazon Athena.
Load the transformed data into Amazon Redshift for analytics and querying.


Techstack
Reddit API: Source of the data.
Apache Airflow & Celery: Orchestrates the ETL process and manages task distribution.
PostgreSQL: Temporary storage and metadata management.
Amazon S3: Raw data storage.
AWS Glue: Data cataloging and ETL jobs.
Amazon Athena: SQL-based data transformation.
Amazon Redshift: Data warehousing and analytics.
Docker: Containerizes the Airflow webserver and other services for a consistent development and production environment.
Power BI: Data visualization tool to generate insights from the processed data.


Workflow

Data Extraction: The project retrieves data from Reddit using the Reddit API.
Data Transformation: The extracted data is cleaned and structured through various transformations.
Data Loading: Both raw and processed data are saved in distinct AWS S3 buckets.
Data Ingestion: Snowpipe automatically imports the data from S3 into Snowflake.
Data Analysis: Data analysis is performed using Power BI, along with additional querying using AWS Athena and Redshift.


Setup Instructions
Clone the repository.
edit the config file name it as 'config.conf' and edit it according to your credentials.
2)Build the Docker containers:
docker-compose up --build

Architecture Diagram

![Architecture Diagram](https://github.com/user-attachments/assets/a915e434-2488-450d-8ced-2256209fe864)
